"""Custom Components store."""
import os

from aiohttp import web
from pyupdate.ha_custom import custom_components
import base_html
import data


PATH = '/config'


async def installed_components_view(request):
    """Default/Installed view"""
    print("Serving default/Installed view.")
    components = await data.get_data()
    installed = []
    content = ''

    for component in components:
        if components[component]['installed']:
            installed.append(component)

    if installed:
        for component in installed:
            if components[component]['has_update']:
                update = '<i class="fa fa-arrow-circle-up">&nbsp;</i>'
            else:
                update = ''
            description = components[component]['description']
            if description is not None and ':' in description:
                description = description.split(':')[-1]
            content += """
              <div class="row">
                <div class="col s12">
                  <div class="card blue-grey darken-1">
                    <div class="card-content white-text">
                      <span class="card-title">{update}{component}</span>
                      <p>{description}</p>
                    </div>
                    <div class="card-action">
                      <a href="/component/{component}">More info</a>
                    </div>
                  </div>
                </div>
              </div>
            """.format(update=update, component=component,
                       description=description)

    else:
        content = """
          <div class="row">
            <div class="col s12">
              <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                  <span class="card-title">No components installed :(</span></a>
                  <p>Go to "The Store" to get some awesome components.</p>
                </div>
              </div>
            </div>
          </div>
        """
    html = base_html.TOP
    html += base_html.BASE.format(main=content)
    html += base_html.END
    return web.Response(body=html, content_type="text/html")



async def the_store_view(request):
    """View for 'The Store'"""
    print("Serving 'The Store'.")
    components = await data.get_data()
    content = ''

    for component in components:
        if components[component]['has_update']:
            update = '<i class="fa fa-arrow-circle-up">&nbsp;</i>'
        else:
            update = ''
        description = components[component]['description']
        if description is not None and ':' in description:
            description = description.split(':')[-1]

        content += """
            <div class="row">
            <div class="col s12">
                <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                    <span class="card-title">{update}{component}</span>
                    <p>{description}</p>
                </div>
                <div class="card-action">
                    <a href="/component/{component}">More info</a>
                </div>
                </div>
            </div>
            </div>
        """.format(update=update, component=component,
                   description=description)

    html = base_html.TOP
    html += base_html.BASE.format(main=content)
    html += base_html.END
    return web.Response(body=html, content_type="text/html")


async def component_view(request):
    """View for single component."""
    component = request.match_info['component']
    print("Serving view for", component)
    components = await data.get_data()

    if component in components:

        button = '<a href="{target}" {extra}>{text}</a>'

        changelog = components[component]['changelog']
        description = components[component]['description']
        has_update = components[component]['has_update']
        image_link = components[component].get('image_link')
        installed = components[component]['installed']
        installed_version = components[component]['local_version']
        published_version = components[component]['version']
        repository = components[component]['visit_repo']

        button1 = button.format(target='/component/'+component+'/install',
                                extra='', text='INSTALL')

        button2 = button.format(target=repository, extra='target="_blank"',
                                text='REPOSITORY')

        button3 = ''

        if installed:
            button1 = button.format(target='/component/'+component,
                                    extra='', text='CHECK FOR UPDATE')

            button4 = button.format(target='/component/'+component+'/uninstall',
                                    extra='class="uninstall"',
                                    text='UNINSTALL')
        else:
            button4 = ''

        if has_update:
            update = '<i class="fa fa-arrow-circle-up">&nbsp;</i>'
            button1 = button.format(target='/component/'+component+'/update',
                                    extra='', text='UPDATE')

            button3 = button.format(target=changelog, extra='target="_blank"',
                                    text='RELEASE NOTES')

        else:
            update = ''

        if description is not None and ':' in description:
            description = description.split(':')[-1]

        if installed_version:
            installed_version = "Installed version: {}".format(installed_version)
        else:
            installed_version = ''

        if image_link:
            image = '</br><img src="{}" class="overview"></br>'.format(image_link)
        else:
            image = ''

        content = """
            <div class="row">
            <div class="col s12">
                <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                    <span class="card-title">{update}{component}</span>
                    <p>
                    {description}</br>
                    {image}</br>
                    {installed_version}</br>
                    Published version: {published_version}</br>
                    </p>
                </div>
                <div class="card-action">
                    {button1}
                    {button2}
                    {button3}
                    {button4}
                </div>
                </div>
            </div>
            </div>
        """.format(update=update, component=component, description=description,
                   image=image, installed_version=installed_version,
                   published_version=published_version, button1=button1,
                   button2=button2, button3=button3, button4=button4)
    else:
        content = """
          <div class="row">
            <div class="col s12">
              <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                  <span class="card-title">Component {component} not found</span></a>
                </div>
              </div>
            </div>
          </div>
        """.format(component=component)

    html = base_html.TOP
    html += base_html.BASE.format(main=content)
    html += base_html.END
    return web.Response(body=html, content_type="text/html")


async def json(request):
    """Serve the response as JSON."""
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
    print("Installing", component)
    custom_components.install(PATH, component, None)
    raise web.HTTPFound('/component/' + component)


async def update_component(request):
    """Update component"""
    component = request.match_info['component']
    print("Updating", component)
    custom_components.install(PATH, component, None)
    raise web.HTTPFound('/component/' + component)


async def uninstall_component(request):
    """Uninstall component"""
    component = request.match_info['component']
    print("Uninstalling", component)
    comp_data = await data.get_data()
    os.remove(PATH + comp_data[component]['local_location'])
    raise web.HTTPFound('/component/' + component)


if __name__ == "__main__":
    DIRECTORY = PATH + '/custom_components'
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    APP = web.Application()
    APP.router.add_route('GET', r'/', installed_components_view)
    APP.router.add_route('GET', r'/store', the_store_view)
    APP.router.add_route('GET', r'/json', json)
    APP.router.add_route('GET', r'/component/{component}', component_view)
    APP.router.add_route('GET', r'/component/{component}/install', install_component)
    APP.router.add_route('GET', r'/component/{component}/update', update_component)
    APP.router.add_route('GET', r'/component/{component}/uninstall', uninstall_component)
    APP.router.add_route('GET', r'/component/{component}/json', json)
    web.run_app(APP, port=9999)
