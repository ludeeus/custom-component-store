"""Custom Components store."""
import os

from aiohttp import web
from pyupdate.ha_custom import custom_components
import base_html
import data


PATH = '/config'


async def about_view(request):
    """View for about."""
    print("Serving about")

    installed_version = os.environ.get('VERSION')
    if not installed_version:
        installed_version = 'dev'

    newest_version = data.get_docker_version()

    content = """
        <div class="row"><div class="col s12">
            <div class="card blue-grey darken-1"><div class="card-content white-text"><span class="card-title">About</span>
                <p>
                    This tool can help you manage your 'custom_components' for Home Assistant.</br>
                    This will <b>only</b> manage the '.py' files for you under 'custom_components/', </br>you still need to manually add/remove entries in 'configuration.yaml'.</br></br>
                    <hr>
                    <div class="row" style="margin-bottom: 2px;">
                        <div class="col s5">Installed version:</div>
                        <div class="col s7">{installed_version}</div>
                    </div>
                    <div class="row" style="margin-bottom: 2px;">
                        <div class="col s5">Newest version:</div>
                        <div class="col s7">{newest_version}</div>
                    </div>
                    <div class="row" style="margin-bottom: 2px;">
                        <div class="col s12"><a href="https://github.com/ludeeus/custom-component-store" target="_blank" class="link">Project @ GitHub</a></div>
                    </div>
                    <div class="row" style="margin-bottom: 2px;">
                        <div class="col s12"><a href="https://hub.docker.com/r/ludeeus/custom-component-store" target="_blank" class="link">Project @ Docker hub</a></div>
                    </div>
                </p>
            </div></div>

            <div class="card blue-grey darken-1"><div class="card-content white-text"><span class="card-title">Custom Components</span>
                <p>
                    All the components/platforms that you can manage with this needs to be added to <a href="https://github.com/ludeeus/customjson" target="_blank" class="link">customjson</a>, 
                    by default all components/platforms that folow the standard in the <a href="https://github.com/custom-components" target="_blank" class="link">custom-component org. on GitHub</a> are managable, other components/platforms would need to be added to <a href="https://github.com/ludeeus/customjson" target="_blank" class="link">customjson</a> before they can show up here.
                </p>
            </div></div>

            <div class="card blue-grey darken-1"><div class="card-content white-text"><span class="card-title">Notice</span>
                <p>
                    This project uses many recources to work:
                    </br><a href="https://github.com/ludeeus/customjson" target="_blank" class="link">customjson</a>
                    </br><a href="https://github.com/ludeeus/pyupdate" target="_blank" class="link">pyupdate</a>
                    </br><a href="https://fontawesome.com/" target="_blank" class="link">Font Awesome</a>
                    </br><a href="http://fonts.googleapis.com/css?family=Roboto" target="_blank" class="link">fonts.googleapis.com</a>
                    </br><a href="https://materializecss.com" target="_blank" class="link">materialize</a>
                    </br><a href="https://aiohttp.readthedocs.io/en/stable/" target="_blank" class="link">aiohttp</a>
                    </br><a href="https://github.com/just-containers/s6-overlay" target="_blank" class="link">s6-overlay</a>
                </p>
            </div></div>

            <div class="card blue-grey darken-1"><div class="card-content white-text">
                <p>
                    <b>This is in the footer of every page here, but I think that it belongs here to.</b></br></br></br>
                    <i>This site and the items here is not created, developed, affiliated, supported, maintained or endorsed by Home Assistant.</i>
                </p>
            </div></div>

            <div class="card blue-grey darken-1"><div class="card-content white-text">
                <p>
                    <a href="https://www.buymeacoffee.com/ludeeus" target="_blank"  class="author"><i class="fa fa-coffee"></i>&nbsp;Buy me a coffee :D</i></a>
                </p>
            </div></div>
        </div></div>
    """.format(installed_version=installed_version, newest_version=newest_version)

    html = base_html.TOP
    html += base_html.BASE.format(main=content)
    html += base_html.END
    return web.Response(body=html, content_type="text/html", charset="utf-8")


async def installed_components_view(request):
    """Default/Installed view."""
    print("Serving default/Installed view")
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
    return web.Response(body=html, content_type="text/html", charset="utf-8")



async def the_store_view(request):
    """View for 'The Store'."""
    print("Serving 'The Store'")
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
    return web.Response(body=html, content_type="text/html", charset="utf-8")


async def component_view(request):
    """View for single component."""
    component = request.match_info['component']
    print("Serving view for", component)
    components = await data.get_data()

    if component in components:

        button = '<a href="{target}" {extra}>{text}</a>'

        authordata = components[component].get('author')
        changelog = components[component]['changelog']
        description = components[component]['description']
        long_description = components[component].get('long_description')
        has_update = components[component]['has_update']
        image_link = components[component].get('image_link')
        installed = components[component]['installed']
        installed_version = components[component]['local_version']
        published_version = components[component]['version']
        repository = components[component]['visit_repo']

        toast = """ onclick=\"M.toast({html: 'Installing', displayLength: 10000})\""""

        button1 = button.format(target='/component/'+component+'/install',
                                extra=toast, text='INSTALL')

        button2 = button.format(target=repository, extra='target="_blank"',
                                text='REPOSITORY')

        button3 = ''

        if authordata:
            author = 'Author: <a href="{}" target="_blank" '.format(authordata.get('html_url'))
            author += 'class="author">@{}</a></br></br>'.format(authordata.get('login'))

        else:
            author = ''

        if installed:
            button1 = button.format(target='/component/'+component,
                                    extra='', text='CHECK FOR UPDATE')

            toast = """ onclick=\"M.toast({html: 'Uninstalling', displayLength: 10000})\""""
            button4 = button.format(target='/component/'+component+'/uninstall',
                                    extra='class="uninstall"'+toast,
                                    text='UNINSTALL')
        else:
            button4 = ''

        if has_update:
            update = '<i class="fa fa-arrow-circle-up">&nbsp;</i>'
            toast = " onclick='M.toast({html: 'Updating', displayLength: 10000)'"
            button1 = button.format(target='/component/'+component+'/update',
                                    extra=toast, text='UPDATE')

            button3 = button.format(target=changelog, extra='target="_blank"',
                                    text='RELEASE NOTES')

        else:
            update = ''

        if description is not None and ':' in description:
            description = description.split(':')[-1]

        if installed_version:
            installed_version = "Installed version: {}</br>".format(installed_version)
        else:
            installed_version = ''

        if image_link:
            image = '</br><img src="{}" class="overview"></br>'.format(image_link)
        else:
            image = ''

        if long_description:
            more_info = '{}</br>'.format(long_description)
        else:
            more_info = ''

        content = """
            <div class="row">
            <div class="col s12">
                <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                    <span class="card-title">{update}{component}</span>
                    <p>
                    {description}</br>
                    {image}</br>
                    {more_info}
                    {author}
                    {installed_version}
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
                   image=image, more_info=more_info, installed_version=installed_version,
                   author=author, published_version=published_version, button1=button1,
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
    return web.Response(body=html, content_type="text/html", charset="utf-8")


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
    APP.router.add_route('GET', r'/about', about_view)
    APP.router.add_route('GET', r'/component/{component}', component_view)
    APP.router.add_route('GET', r'/component/{component}/install', install_component)
    APP.router.add_route('GET', r'/component/{component}/update', update_component)
    APP.router.add_route('GET', r'/component/{component}/uninstall', uninstall_component)
    APP.router.add_route('GET', r'/component/{component}/json', json)
    web.run_app(APP, port=9999)
