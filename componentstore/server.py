"""Custom Components componentstore."""
import os

import componentstore.functions.data as data
import componentstore.functions.manager as manager
from aiohttp import web
from aiohttp_basicauth import BasicAuthMiddleware


REASON = None
REDIS_HOST = None
REDIS_PORT = None
NO_CACHE = False


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
    json_data = await data.get_data(component=component)
    return web.json_response(json_data)


async def install_component(request):
    """Install component"""
    component = request.match_info['component']
    requester = request.headers.get('X-FORWARDED-FOR', None)
    print("Installing/updating", component, "requested by", requester)
    await manager.install_component(component)
    await data.get_data(True)
    raise web.HTTPFound('/component/' + component)


async def uninstall_component(request):
    """Uninstall component"""
    component = request.match_info['component']
    requester = request.headers.get('X-FORWARDED-FOR', None)
    print("Uninstalling", component, "requested by", requester)
    await manager.uninstall_component(component)
    await data.get_data(True)
    raise web.HTTPFound('/component/' + component)


async def migrate_component(request):
    """Migrate component"""
    component = request.match_info['component']
    requester = request.headers.get('X-FORWARDED-FOR', None)
    print("Migrating", component, "requested by", requester)
    await manager.migrate_component(component)
    await data.get_data(True)
    raise web.HTTPFound('/component/' + component)


async def reloadinstalled(request):  # pylint: disable=W0613
    """Reload"""
    await data.get_data(True)
    raise web.HTTPFound('/')


async def reloadstore(request):  # pylint: disable=W0613
    """Reload"""
    await data.get_data(True)
    raise web.HTTPFound('/store')


def run_server(
        ha_path, username, password, no_auth, port=9999, redis_host=None,
        redis_port=None, nocache=False):
    """Run the webserver."""
    print("Custom-component-store is starting.")
    global REASON  # pylint: disable=W0603
    global REDIS_HOST # pylint: disable=W0603
    global REDIS_PORT  # pylint: disable=W0603
    global NO_CACHE  # pylint: disable=W0603

    if ha_path:
        print(ha_path)
        os.environ["HA_CONFIG_PATH"] = ha_path

    if redis_host is None:
        REDIS_HOST = os.environ.get('REDIS_HOST')
    else:
        REDIS_HOST = redis_host

    if redis_host is None:
        REDIS_HOST = os.environ.get('REDIS_PORT')
    else:
        REDIS_PORT = redis_port

    if nocache is None:
        NO_CACHE = os.environ.get('NO_CACHE')
    else:
        NO_CACHE = nocache

    path = os.environ.get('HA_CONFIG_PATH', '/config')

    directory = path + '/custom_components'
    version_path = path + '/.HA_VERSION'
    version = 0
    target = 86

    if not no_auth:
        auth = BasicAuthMiddleware(username=username, password=password)
        app = web.Application(middlewares=[auth])
    else:
        app = web.Application()

    if not os.path.exists(version_path):
        REASON = 'ha_not_found'

    elif not os.path.exists(path):
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

    if not NO_CACHE:
        redis = data.redis_connect()

        if not redis:
            REASON = 'redis_conn_error'
    else:
        print('Cache disabled...')

    if REASON is None:
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
        app.router.add_route(
            'GET', r'/reloadinstalled', reloadinstalled)
        app.router.add_route(
            'GET', r'/reloadstore', reloadstore)
    else:
        print("There was an issue starting", REASON)
        app.router.add_route(
            'GET', r'/', error_view)
        app.router.add_route(
            'GET', r'/{route}', error_view)
    web.run_app(app, port=port, print=None)
