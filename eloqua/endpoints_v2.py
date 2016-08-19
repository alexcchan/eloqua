"""
API MAPPING FOR Eloqua API V2
"""

mapping_table = {

    'content_type': 'application/json',
    'path_prefix': '/API/REST/2.0',

    # Campaigns
    'get_campaign': {
        'method': 'GET',
        'path': '/assets/campaign/{{campaign_id}}',
        'valid_params': ['depth']
    },
    'list_campaigns': {
        'method': 'GET',
        'path': '/assets/campaigns',
        'valid_params': ['depth','count','page','search','sort','dir','orderBy','lastUpdatedAt']
    },
    'create_campaign': {
        'method': 'POST',
        'path': '/assets/campaign',
        'status': 201
    },
    'update_campaign': {
        'method': 'PUT',
        'path': '/assets/campaign/{{campaign_id}}'
    },
    'activate_campaign': {
        'method': 'POST',
        'path': '/assets/campaign/active/{{campaign_id}}',
        'valid_params': ['activateNow','scheduledFor','runAsUserId'],
        'status': 201
    },

    # Campaign folders - UNDOCUMENTED
    'get_campaign_folder': {
        'method': 'GET',
        'path': '/assets/campaign/folder/{{campaign_folder_id}}',
        'valid_params': ['depth']
    },
    'list_campaign_folders': {
        'method': 'GET',
        'path': '/assets/campaign/folders',
        'valid_params': ['depth','count','page','search','sort','dir','orderBy','lastUpdatedAt']
    },

}
