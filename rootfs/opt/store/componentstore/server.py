"""Custom Components componentstore."""
import os

import componentstore.functions.data as data
import componentstore.functions.manager as manager
from aiohttp import web


PATH = '/config'
REASON = None


async def error_view(request):  # pylint: disable=W0613
    """View for about."""
    from componentstore.view.error import view
    requester = request.headers.get('X-FORWARDED-FOR', None)
    print("Serving error to", requester)
    html = await view()
    return web.Response(body=html, content_type="text/html", charset="utf-8")


async def about_view(request):  # pylint: disable=W0613
    """View for about."""
    from componentstore.view.about import view
    requester = request.headers.get('X-FORWARDED-FOR', None)
    print("Serving about to", requester)
    html = await view()
    return web.Response(body=html, content_type="text/html", charset="utf-8")


async def installed_components_view(request):  # pylint: disable=W0613
    """Default/Installed view."""
    from componentstore.view.component.installed import view
    requester = request.headers.get('X-FORWARDED-FOR', None)
    print("Serving default/Installed view to", requester)
    html = await view()
    return web.Response(body=html, content_type="text/html", charset="utf-8")



async def the_store_view(request):  # pylint: disable=W0613
    """View for 'The Store'."""
    from componentstore.view.component.the_store import view
    requester = request.headers.get('X-FORWARDED-FOR', None)
    print("Serving 'The Store' to", requester)
    html = await view()
    return web.Response(body=html, content_type="text/html", charset="utf-8")


async def component_view(request):
    """View for single component."""
    from componentstore.view.component.component import view
    requester = request.headers.get('X-FORWARDED-FOR', None)
    component = request.match_info['component']
    print("Serving view for", component, "to", requester)
    html = await view(component)
    return web.Response(body=html, content_type="text/html", charset="utf-8")


async def json(request):
    """Serve the response as JSON."""
    requester = request.headers.get('X-FORWARDED-FOR', None)
    print("Serving JSON requested by", requester)
    try:
        component = request.match_info['component']
    except:
        component = None
    json_data = await data.get_data()
    if component:
        json_data = json_data[component]
    return web.json_response(json_data)


async def install_component(request):
    """Install component"""
    component = request.match_info['component']
    requester = request.headers.get('X-FORWARDED-FOR', None)
    print("Installing/updating", component, "requested by", requester)
    await manager.install_component(component)
    raise web.HTTPFound('/component/' + component)


async def uninstall_component(request):
    """Uninstall component"""
    component = request.match_info['component']
    requester = request.headers.get('X-FORWARDED-FOR', None)
    print("Uninstalling", component, "requested by", requester)
    await manager.uninstall_component(component)
    raise web.HTTPFound('/component/' + component)


async def migrate_component(request):
    """Migrate component"""
    component = request.match_info['component']
    requester = request.headers.get('X-FORWARDED-FOR', None)
    print("Migrating", component, "requested by", requester)
    await manager.migrate_component(component)
    raise web.HTTPFound('/component/' + component)


def run_server(port=9999):
    """Run the webserver."""
    global REASON  # pylint: disable=W0603
    directory = PATH + '/custom_components'
    version_path = PATH + '/.HA_VERSION'
    version = 0
    target = 86

    app = web.Application()

    if not os.path.exists(version_path):
        REASON = 'ha_not_found'

    elif not os.path.exists(PATH):
        REASON = 'no_path'

    else:
        with open(version_path) as version_file:
            version = version_file.readlines()
            version = int(version[0].split('.')[1])

        if version < target:
            REASON = 'version'
            print("HA Version", version)

        if not os.path.exists(directory):
            os.makedirs(directory)

    if REASON is None:
        print("Custom-component-store is starting.")
        app.router.add_route(
            'GET', r'/', installed_components_view)
        app.router.add_route(
            'GET', r'/about', about_view)
        app.router.add_route(
            'GET', r'/component/{component}', component_view)
        app.router.add_route(
            'GET', r'/component/{component}/install', install_component)
        app.router.add_route(
            'GET', r'/component/{component}/json', json)
        app.router.add_route(
            'GET', r'/component/{component}/migrate', migrate_component)
        app.router.add_route(
            'GET', r'/component/{component}/uninstall', uninstall_component)
        app.router.add_route(
            'GET', r'/component/{component}/update', install_component)
        app.router.add_route(
            'GET', r'/json', json)
        app.router.add_route(
            'GET', r'/store', the_store_view)
    else:
        print("There was an issue starting", REASON)
        app.router.add_route(
            'GET', r'/', error_view)
        app.router.add_route(
            'GET', r'/{route}', error_view)
    web.run_app(app, port=port, print=None)
