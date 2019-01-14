"""Handle data"""
import os
import re
import requests
from pyupdate.ha_custom import custom_components


PATH = '/config'


async def get_data():
    """Get version data."""
    value = {}
    url = 'https://raw.githubusercontent.com/custom-components/information'
    url += '/master/repos.json'
    web_request = requests.get(url).json()

    local_components = get_local_components()

    if web_request:
        for item in web_request:
            value[item] = web_request[item]

    extra = os.environ.get('EXTRA')
    if extra:
        extra_request = requests.get(extra).json()
        for item in extra_request:
            value[item] = extra_request[item]


        for item in value:
            local_locations = []
            local_path = None
            installed = False
            has_update = False
            version = None

            if value[item].get('embedded_path') is not None:
                local_locations.append(value[item].get('embedded_path'))
            if not local_locations:
                local_locations.append(value[item].get('local_location'))

            for path in local_locations:
                print(path)
                if path in local_components:
                    local_path = path
                    installed = True
                    break
                print(path, installed)

            if installed:
                version = get_local_version(local_path)
            if version is not None:
                has_update = version != value[item]['version']

            value[item]['local_version'] = version
            value[item]['has_update'] = has_update
            value[item]['has_update'] = has_update
            value[item]['installed'] = installed
    return value


def get_docker_version():
    """Get version published for docker."""
    version = None
    url = 'https://registry.hub.docker.com/v2/repositories/'
    url += 'ludeeus/custom-component-store/tags/'
    tags = requests.get(url).json()['results']
    for tag in tags:
        if tag['name'] not in ['latest', 'dev']:
            version = tag['name']
            break
    return version

def migration_needed(component):
    """Return bool if migration is needed."""
    value = False
    if '.' in component:
        domain = component.split('.')[0]
        platform = component.split('.')[1]

        old_format_file_location = "{}/{}/{}/{}.py".format(PATH,
                                                           'custom_components',
                                                           domain, platform)
        print(old_format_file_location)
        if os.path.exists(old_format_file_location):
            value = True
    return value

def get_local_components():
    """Local components and platforms."""
    base = PATH + '/custom_components/'
    components = []
    accepted = []
    domains = os.listdir(base)
    for domain in domains:
        platforms = os.listdir(base + domain)
        for platform in platforms:
            components.append("{}{}/{}".format('/custom_components/', domain, platform))
    for item in components:
        if get_local_version(item) is not None:
            accepted.append(item)
    return accepted


def get_local_version(path):
    """Return the local version if any."""
    path = PATH + path
    return_value = None
    if os.path.isfile(path):
        with open(path, 'r') as local:
            ret = re.compile(r"^\b(VERSION|__version__)\s*=\s*['\"](.*)['\"]")
            for line in local.readlines():
                matcher = ret.match(line)
                if matcher:
                    return_value = str(matcher.group(2))
    return return_value
