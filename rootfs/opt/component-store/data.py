"""Handle data"""
import os
import requests
from pyupdate.ha_custom import custom_components


PATH = '/config'


async def get_data():
    """Get version data."""
    value = {}
    url = 'https://raw.githubusercontent.com/custom-components/information'
    url += '/master/repos.json'
    web_request = requests.get(url).json()

    if web_request:
        for item in web_request:
            value[item] = web_request[item]
            value[item]['local_version'] = None
            value[item]['installed'] = False
            value[item]['has_update'] = False

    local_components = {}

    extra = os.environ.get('EXTRA')

    local_request = custom_components.get_sensor_data(PATH, False, extra)[0]

    for item in local_request:
        if item not in ['domain', 'has_update']:
            local_components[item] = local_request[item]

    if local_components:
        for item in local_components:
            local_version = local_components[item].get('local')
            has_update = local_components[item].get('has_update')
            value[item]['local_version'] = local_version
            value[item]['installed'] = True
            value[item]['has_update'] = has_update

    return value
