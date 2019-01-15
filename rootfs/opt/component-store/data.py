"""Handle data"""
import os
import re
import requests


PATH = '/config'
DOMAINS = ['sensor', 'switch', 'media_player', 'climate', 'light', 'binary_sensor']
DATA = {}

EXAMPLE = {
    "sensor.example": {
        "trackable": True,
        "embedded_path": "/custom_components/example/sensor.py",
        "version": os.environ.get('VERSION'),
        "installed": False,
        "visit_repo": "https://github.com/ludeeus/custom-component-store",
        "embedded_path_remote": "https://github.com/ludeeus/custom-component-store",
        "changelog": "https://github.com/ludeeus/custom-component-store",
        "embedded": True,
        "has_update": False,
        "local_location": "/custom_components/sensor/example.py",
        "local_version": os.environ.get('VERSION'),
        "author": {
            "login": "ludeeus",
            "html_url": "https://github.com/ludeeus"
        },
        "description": "Example sensor entity.",
        "remote_location": "https://github.com/ludeeus/custom-component-store"
    }
}

async def get_data():
    """Get data."""
    global DATA
    try:
        value = {}
        url = 'https://raw.githubusercontent.com/custom-components/information'
        url += '/master/repos.json'
        web_request = requests.get(url).json()

        local_components = get_local_components()

        if web_request:
            for item in web_request:
                if web_request[item]['version'] is None:
                    continue
                value[item] = web_request[item]

        extra = os.environ.get('EXTRA')
        if extra:
            extra_request = requests.get(extra).json()
            for item in extra_request:
                if extra_request[item]['version'] is None:
                    continue
                value[item] = extra_request[item]


        for item in value:
            local_locations = []
            local_path = None
            installed = False
            has_update = False
            version = None

            local_locations.append(value[item].get('embedded_path'))
            local_locations.append(value[item].get('local_location'))

            for path in local_locations:
                if path in local_components:
                    local_components.remove(path)
                    local_path = path
                    installed = True

            if installed:
                version = get_local_version(local_path)
            if version is not None:
                has_update = version != value[item]['version']

            value[item]['local_version'] = version
            value[item]['has_update'] = has_update
            value[item]['has_update'] = has_update
            value[item]['installed'] = installed
            value[item]['trackable'] = True


        for item in local_components:
            local_location = item
            name = item.split('/custom_components/')[1].split('.py')[0]

            if '__init__' in name:
                name = name.split('/')[0]

            elif '/' in name:
                domain = name.split('/')[0]
                platform = name.split('/')[1]
                if domain in DOMAINS:
                    name = "{}.{}".format(domain, platform)
                else:
                    name = "{}.{}".format(domain, platform)

            value[name] = {}
            value[name]['trackable'] = False
            value[name]['installed'] = True
            value[name]['local_location'] = local_location

        DATA = value
    except Exception as error:
        print("There was an issue getting new data!")
        print(error)
    return DATA


def migration_needed(component):
    """Return bool if migration is needed."""
    value = False
    if '.' in component:
        domain = component.split('.')[0]
        platform = component.split('.')[1]

        old_format_file_location = "{}/{}/{}/{}.py".format(PATH,
                                                           'custom_components',
                                                           domain, platform)
        if os.path.exists(old_format_file_location):
            value = True
    return value

def get_local_components():
    """Local components and platforms."""
    base = PATH + '/custom_components/'
    components = []
    domains = []
    for domain in os.listdir(base):
        if '.py' in domain:
            components.append("{}{}".format('/custom_components/', domain))
        else:
            domains.append(domain)

    for domain in domains:
        for platform in os.listdir(base + domain):
            components.append("{}{}/{}".format('/custom_components/', domain, platform))

    return components


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
