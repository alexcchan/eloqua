"""
   Wrapper for the Eloqua API.  Based on the Python Zendesk library by Max
   Gutman <max@eventbrite.com>.
"""


import base64
import httplib2
import re
import urllib
try:
    import simplejson as json
except:
    import json

from datetime import datetime
from endpoints_bulk_v2 import mapping_table as mapping_table_bulk
from endpoints_v1 import mapping_table as mapping_table_v1
from endpoints_v2 import mapping_table as mapping_table_v2
from httplib import responses


ELOQUA_LOGIN_URL = 'https://login.eloqua.com/id'
DEFAULT_HTTP_METHOD = 'GET'
DEFAULT_HTTP_STATUS_CODE = 200
DEFAULT_CONTENT_TYPE = 'application/json'


class EloquaError(Exception):
    def __init__(self, msg, error_code=None):
        self.msg = msg
        self.error_code = error_code

    def __str__(self):
        return repr('%s: %s' % (self.error_code, self.msg))


def clean_kwargs(kwargs):
    for key, value in kwargs.iteritems():
        if hasattr(value, '__iter__'):
            kwargs[key] = ','.join(map(str, value))
#    underscore_keys = [key for key in kwargs if key.find('_')>=0]
#    for key in underscore_keys:
#        val = kwargs.pop(key)
#        kwargs[key.replace('_','-')] = val


class Eloqua(object):

    def __init__(self, username, password, api_version=1, base_url=None, client_args={}):
        self.username = username
        self.password = password
        if api_version == 0:
            self.mapping_table = mapping_table_bulk
        elif api_version == 1:
            self.mapping_table = mapping_table_v1
        elif api_version == 2:
            self.mapping_table = mapping_table_v2
        else:
            raise ValueError("Unsupported Eloqua API Version: %d" %
                    api_version)
        self.client = httplib2.Http(**client_args)
        if base_url is None:
            self._init_base_url()
        else:
            self.base_url = base_url

    def __getattr__(self, api_call):
        def call(self, **kwargs):
            api_map = self.mapping_table[api_call]
            method = api_map.get('method', DEFAULT_HTTP_METHOD)
            status = api_map.get('status', DEFAULT_HTTP_STATUS_CODE)
            valid_params = api_map.get('valid_params', [])
            body = kwargs.pop('data', None)
            api_map_path = api_map.get('path','')
            if api_map_path.startswith('https://'):
                url_template = api_map_path
            else:
                path = self.mapping_table.get('path_prefix','') + api_map_path
                url_template = self.base_url + path
            url = re.sub(
                    '\{\{(?P<m>[a-zA-Z_]+)\}\}',
                    lambda m: "%s" % urllib.quote(str(kwargs.pop(m.group(1),''))),
                    url_template
            )
            clean_kwargs(kwargs)
            for kw in kwargs:
                if kw not in valid_params:
                    raise TypeError("%s() got an unexpected keyword argument "
                            "'%s'" % (api_call, kw))
            url += '?' + urllib.urlencode(kwargs)
            return self._make_request(method, url, body, status)
        return call.__get__(self)

    def _get_authorization(self):
        return base64.b64encode('%s:%s' % (self.username,self.password))

    def _init_base_url(self):
        headers = {}
        headers["Authorization"] = "Basic %s" % self._get_authorization()
        response,content = self.client.request(ELOQUA_LOGIN_URL,headers=headers)
        self.base_url = json.loads(content)['urls']['base']

    def _make_request(self, method, url, body, status):
        headers = {}
        headers["Authorization"] = "Basic %s" % self._get_authorization()
        if body:
            content_type = self.mapping_table.get('content_type', DEFAULT_CONTENT_TYPE)
            headers["Content-Type"] = content_type
            if isinstance(body, dict):
                if content_type == 'application/x-www-form-urlencoded':
                    body = urllib.urlencode(body)
                elif content_type == 'application/json':
                    body = json.dumps(body)
            elif isinstance(body,list):
                if content_type == 'application/json':
                    body = json.dumps(body)
        response,content = self.client.request(url, method=method, body=body,
                headers=headers)
        return self._response_handler(response, content, status)

    def _response_handler(self, response, content, status):
        if not response:
            raise EloquaError('Response Not Found')
        response_status = int(response.get('status', 0))
        if response_status != status:
            raise EloquaError(content, response_status)
        if response.get('location'):
            return response.get('location')
        elif content.strip():
            return json.loads(content)
        else:
            return responses[response_status]

    @staticmethod
    def date_string(d=None):
        """Format date/time according to Eloqua ISO 8601."""
        if d is None:
            d = datetime.utcnow()
        return d.strftime('%Y-%m-%dT%H:%M:%SZ')
