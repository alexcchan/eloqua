"""
API MAPPING FOR Eloqua API V1
"""

mapping_table = {

    'content_type': 'application/json',
    'path_prefix': '/API/REST/1.0',

    # Contact lists
    'get_contact_list': {
        'method': 'GET',
        'path': '/assets/contact/list/{{contact_list_id}}',
        'valid_params': ['depth']
    },
    'list_contact_lists': {
        'method': 'GET',
        'path': '/assets/contact/lists',
        'valid_params': ['depth','count','page','search','sort','dir','orderBy','lastUpdatedAt']
    },

    # Contact list folders - UNDOCUMENTED
    'get_contact_list_folder': {
        'method': 'GET',
        'path': '/assets/contact/list/folder/{{contact_list_folder_id}}',
        'valid_params': ['depth']
    },
    'list_contact_list_folders': {
        'method': 'GET',
        'path': '/assets/contact/list/folders',
        'valid_params': ['depth','count','page','search','sort','dir','orderBy','lastUpdatedAt']
    },

    # Contact segments
    'get_contact_segment': {
        'method': 'GET',
        'path': '/assets/contact/segment/{{contact_segment_id}}',
        'valid_params': ['depth']
    },
    'list_contact_segments': {
        'method': 'GET',
        'path': '/assets/contact/segments',
        'valid_params': ['depth','count','page','search','sort','dir','orderBy','lastUpdatedAt']
    },

    # Contact segment folders - UNDOCUMENTED
    'get_contact_segment_folder': {
        'method': 'GET',
        'path': '/assets/contact/segment/folder/{{contact_segment_folder_id}}',
        'valid_params': ['depth']
    },
    'list_contact_segment_folders': {
        'method': 'GET',
        'path': '/assets/contact/segment/folders',
        'valid_params': ['depth','count','page','search','sort','dir','orderBy','lastUpdatedAt']
    },

    # Emails
    'get_email': {
        'method': 'GET',
        'path': '/assets/email/{{email_id}}',
        'valid_params': ['depth']
    },
    'list_emails': {
        'method': 'GET',
        'path': '/assets/emails',
        'valid_params': ['depth','count','page','search','sort','dir','orderBy','lastUpdatedAt']
    },

    # Email folders
    'get_email_folder': {
        'method': 'GET',
        'path': '/assets/email/folder/{{email_folder_id}}',
        'valid_params': ['depth']
    },
    'list_email_folders': {
        'method': 'GET',
        'path': '/assets/email/folders',
        'valid_params': ['depth','count','page','search','sort','dir','orderBy','lastUpdatedAt']
    },

    # Email groups
    'list_email_groups': {
        'method': 'GET',
        'path': '/assets/email/groups',
        'valid_params': ['depth','count','page','search','sort','dir','orderBy','lastUpdatedAt']
    },

    # Templates
    'get_template': {
        'method': 'GET',
        'path': '/assets/template/{{template_id}}',
        'valid_params': ['depth']
    },
    'list_templates': {
        'method': 'GET',
        'path': '/assets/templates',
        'valid_params': ['depth','count','page','search','sort','dir','orderBy','lastUpdatedAt']
    },

}
