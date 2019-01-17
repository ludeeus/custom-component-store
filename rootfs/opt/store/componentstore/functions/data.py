"""Handle data"""
import os
import re
import requests
from componentstore.const import DOMAINS, PATH


DATA = {}


async def get_data():  # pylint: disable=R0912,R0914,R0915
    """Get data."""
    global DATA  # pylint: disable=W0603
    try:
        value = {}
        url = 'https://raw.githubusercontent.com/'
        url += 'ludeeus/data/'
        url += 'master/'
        url += 'custom-component-store/'
        url += 'V1'
        url += '/data.json'
        web_request = requests.get(url).json()

        local_components = await get_local_components()

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
                version = await get_local_version(local_path)
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
    except Exception as error:  # pylint: disable=W0703
        print("There was an issue getting new data!")
        print("Cached data will be used to next run.")
        print(error)
    return DATA


async def migration_needed(component):
    """Return bool if migration is needed."""
    value = False
    if '.' in component:
        domain = component.split('.')[0]
        platform = component.split('.')[1]

        old_format_file_location = "{}/{}/{}/{}.py".format(
            PATH, 'custom_components', domain, platform)
        if os.path.exists(old_format_file_location):
            value = True
    return value


async def get_local_components():
    """Local components and platforms."""
    base = PATH + '/custom_components/'
    components = []
    accepted = []
    domains = []
    for domain in os.listdir(base):
        if '.py' in domain:
            components.append("{}{}".format('/custom_components/', domain))
        else:
            domains.append(domain)

    for domain in domains:
        for platform in os.listdir(base + domain):
            components.append("{}{}/{}".format(
                '/custom_components/', domain, platform))

    for component in components:
        if '__pycache__' in component:
            continue
        if '.pyc' in component:
            continue
        if not '.py' in component:
            continue
        accepted.append(component)
    return accepted


async def get_local_version(path):
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
