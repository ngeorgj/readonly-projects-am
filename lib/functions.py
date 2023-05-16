#
# Salinas Research, 2022
#                                                 Research & Development Branch
#
# Original Filename: functions
# on 16/May/2023
#
# Extra Comments on File
#
#
import json

import requests

from config import credentials, base_url


# Local Library Imports

# Other Imports

headers = {'Content-Type': "application/json"}

# WEB REQUESTS
def get(url, header={}, params={}):
    # Send a GET request with the specified URL, headers, authentication, and parameters
    return requests.get(
        url,
        headers=header,
        auth=credentials,
        params=params
    )


def post(url, data, header=headers, params={}):
    return requests.post(
        url,
        headers=header,
        data=json.dumps(data),  # Convert data to JSON format
        auth=credentials,
        params=params
    )


def put(url, data, header=headers, params={}):
    return requests.put(
        url,
        headers=header,
        data=json.dumps(data),  # Convert data to JSON format
        auth=credentials,
        params=params
    )


def get_projects():
    return get(base_url + '/rest/api/2/project').json()


# Main Function
def set_permission_scheme(scheme_id, project_key):
    url = base_url + f'/rest/api/2/project/{project_key}/permissionscheme'
    payload = {'id': int(scheme_id)}
    result = put(url, payload)
    if result.status_code == 200:
        print(f'Project [{project_key}] Permission scheme updated to {scheme_id}')
        return result


def create_read_only_permission_scheme(name="[CPRIME] READONLY PERMISSION SCHEME"):
    permissions = get(base_url + '/rest/api/2/permissions').json()['permissions']
    permissions_list = [permission['key'] for _, permission in permissions.items() if permission['type'] == 'PROJECT']
    generative_object = {
        "name": name,
        "description": "This permission scheme will be applied in the migrated projects as a post-migration remediation.",
        "permissions": [
            {
                "holder": {
                    "type": "group",
                    "parameter": "jira-administrators"
                },
                "permission": permission
            } for permission in permissions_list
        ]
    }
    result = post(base_url + '/rest/api/2/permissionscheme', generative_object)
    if result.status_code == 201:
        print(f'Permission Scheme: {name} has been created!')
    else:
        return print('Some error occurred during the scheme creation.')

    return result.json()
