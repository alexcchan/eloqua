"""
API MAPPING FOR Eloqua Bulk API V2
"""

mapping_table = {

    'content_type': 'application/json',
    'path_prefix': '/api/bulk/2.0',

    # Contacts export
    'create_contacts_export': {
        'method': 'POST',
        'path': '/contacts/exports',
        'status': 201
    },
    'get_contacts_export_data': {
        'method': 'GET',
        'path': '/contacts/exports/{{export_id}}/data',
        'valid_params': ['limit','offset','totalResults']
    },
    'delete_contacts_export_data': {
        'method': 'DELETE',
        'path': '/contacts/exports/{{export_id}}/data',
        'status': 204
    },

    # Contacts import
    'create_contacts_import': {
        'method': 'POST',
        'path': '/contacts/imports',
        'status': 201
    },
    'create_contacts_import_data': {
        'method': 'POST',
        'path': '/contacts/imports/{{import_id}}/data',
        'status': 204
    },
    'delete_contacts_import_data': {
        'method': 'DELETE',
        'path': '/contacts/imports/{{import_id}}/data',
        'status': 204
    },

    # Syncs
    'get_sync': {
        'method': 'GET',
        'path': '/syncs/{{sync_id}}'
    },
    'get_sync_data': {
        'method': 'GET',
        'path': '/syncs/{{sync_id}}/data'
    },
    'create_sync': {
        'method': 'POST',
        'path': '/syncs',
        'status': 201
    },
}
