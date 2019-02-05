"""Handle data"""
import json
import os
import re

import requests

import redis
from componentstore.const import DOMAINS, REDIS_TOPIC_BASE

REDIS = None


async def get_data(force=False, component=None):  # pylint: disable=R0912,R0914,R0915
    """Get data."""
    from componentstore.server import NO_CACHE
    if not NO_CACHE:
        if not force:
            cache = await redis_get()
            if cache:
                print("Loaded data from redis.")
                if component:
                    cache = cache[component]
                return cache
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

        if not NO_CACHE:
            await redis_set(value)
        else:
            data = value
    except Exception as error:  # pylint: disable=W0703
        print("There was an issue getting new data!")
        print("Cached data will be used untill next run.")
        print(error)
    if not NO_CACHE:
        cache = await redis_get()
        data = cache
    if component:
        data = data[component]
    return data


async def migration_needed(component):
    """Return bool if migration is needed."""
    configpath = os.environ.get('HA_CONFIG_PATH', '/config')
    value = False
    if '.' in component:
        domain = component.split('.')[0]
        platform = component.split('.')[1]

        old_format_file_location = "{}/{}/{}/{}.py".format(
            configpath, 'custom_components', domain, platform)
        if os.path.exists(old_format_file_location):
            value = True
    return value


async def get_local_components():
    """Local components and platforms."""
    configpath = os.environ.get('HA_CONFIG_PATH', '/config')
    base = configpath + '/custom_components/'
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
    configpath = os.environ.get('HA_CONFIG_PATH', '/config')
    path = configpath + path
    return_value = None
    if os.path.isfile(path):
        with open(path, 'r') as local:
            ret = re.compile(r"^\b(VERSION|__version__)\s*=\s*['\"](.*)['\"]")
            for line in local.readlines():
                matcher = ret.match(line)
                if matcher:
                    return_value = str(matcher.group(2))
    return return_value


async def redis_set(data):
    """Write data to redis."""
    if REDIS is None:
        redis_connect()
    print("Writing data to redis.")
    REDIS.set(REDIS_TOPIC_BASE, json.dumps(data))


async def redis_get():
    """Get data from redis."""
    if REDIS is None:
        redis_connect()
    try:
        data = REDIS.get(REDIS_TOPIC_BASE)
        data = json.loads(data)
    except Exception as error:  # pylint: disable=W0703
        print(error)
        data = None
    return data

def redis_connect():
    """Connect to redis server."""
    from componentstore.server import REDIS_HOST, REDIS_PORT
    global REDIS  # pylint: disable=W0603
    print("Connecting to redis server.")
    try:
        if REDIS_HOST is None:
            client = redis.StrictRedis(decode_responses=True)
        else:
            client = redis.StrictRedis(
                host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        REDIS = client
        return True
    except Exception as error:  # pylint: disable=W0703
        print(error)
        return False
