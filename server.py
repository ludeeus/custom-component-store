"""Run the server for hachanges."""
import os

import requests

import static
from aiohttp import web
from pyupdate.ha_custom import custom_components

PATH = '/config'

async def install(request):
    """Install component"""
    element = request.match_info['element']
    custom_components.install(PATH, element, None)
    raise web.HTTPFound('/component/' + element)

async def uninstall(request):
    """Install component"""
    element = request.match_info['element']
    data = await get_data()
    os.remove(PATH + data[element]['local_location'])
    raise web.HTTPFound('/component/' + element)

async def installed(request):
    """Serve a HTML site."""
    content = static.STYLE

    content += static.HEADER

    content += '<main>'
    resp = custom_components.get_sensor_data(PATH, False, None)[0]
    compdata = await get_data()
    components = []
    for item in resp:
        if item not in ['domain', 'has_update']:
            components.append(item)
    if not components:
        content += static.NOCOMPONENTS
    for component in components:
        update = ''
        comp = component
        version = compdata[component].get('version')
        installedver = resp[component].get('local')
        if version != installedver:
            update = static.UPDATE
        description = compdata[component].get('description', '')
        repo = compdata[component].get('visit_repo')
        if description is not None and ':' in description:
            description = description.split(':')[-1]
        content += static.CARD.format(comp=comp, update=update,
                                      version=version,
                                      content=description,
                                      target='/component/'+comp,
                                      button='More info',
                                      repo=repo, extra='')
    content += '</main>'
    content += static.FOOTER
    return web.Response(body=content, content_type="text/html")

async def html(request):
    """Serve a HTML site."""
    content = static.STYLE

    content += static.HEADER

    content += '<main>'

    components = await get_data()

    for component in components:
        comp = component
        version = components[component].get('version')
        description = components[component].get('description', '')
        repo = components[component].get('visit_repo')
        if description is not None and ':' in description:
            description = description.split(':')[-1]
        content += static.CARD.format(comp=comp, update='',
                                      version=version,
                                      content=description,
                                      target='/component/'+comp,
                                      button='More info',
                                      repo=repo, extra='')
    content += '</main>'
    content += static.FOOTER
    return web.Response(body=content, content_type="text/html")

async def compview(request):
    """Serve a HTML site."""
    element = request.match_info['element']
    content = static.STYLE

    content += static.HEADER

    content += '<main>'

    components = await get_data()
    hasupdate = False
    update = ''
    compdata = await get_comp_data(element)
    installedver = compdata.get('local')
    component = components[element]
    comp = element
    version = component.get('version')
    description = component.get('description', '')
    repo = component.get('visit_repo')
    extra = static.REPO.format(repo=repo)
    target = '/component/' + comp + '/install'
    if description is not None and ':' in description:
        description = description.split(':')[-1]
    if installedver:
        if installedver != version:
            hasupdate = True
        if hasupdate:
            button = 'Update'
            update = static.UPDATE
            extra += static.NOTES.format(notes=component.get('changelog'))
        else:
            button = 'Check for update'
            target = '/component/' + comp
        extra += static.UNINSTALL.format(uninstall='/component/'+comp+'/uninstall')
    else:
        installedver = 'N/A'
        button = 'Install'
    description += static.CONTENT.format(version=version, installed=installedver)
    content += static.CARD.format(comp=comp, update=update,
                                  version=version,
                                  content=description,
                                  target=target,
                                  button=button,
                                  extra=extra)
    content += '</main>'
    content += static.FOOTER
    return web.Response(body=content, content_type="text/html")

async def json(request):
    """Serve the response as JSON."""
    json_data = custom_components.get_sensor_data(PATH, True, None)[0]
    return web.json_response(json_data)

async def compjson(request):
    """Serve the response as JSON."""
    element = request.match_info['element']
    json_data = await get_data()
    return web.json_response(json_data[element])

async def get_comp_data(name=None):
    """get comp data"""
    data = custom_components.get_sensor_data(PATH, True, None)[0]
    return data[name]

async def get_data():
    """Get version data."""
    url = 'https://raw.githubusercontent.com/custom-components/information/master/repos.json'
    data = requests.get(url).json()

    if data:
        value = data
    else:
        value = None

    return value

if __name__ == "__main__":
    DIRECTORY = PATH + '/custom_components'
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    APP = web.Application()
    APP.router.add_route('GET', r'/', installed, name='installed')
    APP.router.add_route('GET', r'/components', html, name='html')
    APP.router.add_route('GET', r'/json', json, name='json')
    APP.router.add_route('GET', r'/component/{element}', compview, name='compview')
    APP.router.add_route('GET', r'/component/{element}/install', install, name='install')
    APP.router.add_route('GET', r'/component/{element}/uninstall', uninstall, name='uninstall')
    APP.router.add_route('GET', r'/component/{element}/json', compjson, name='compjson')
    web.run_app(APP, port=9999)
