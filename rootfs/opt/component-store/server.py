"""Custom Components store."""
import os

import requests

import base_html
import data
from aiohttp import web

PATH = data.PATH


async def about_view(request):
    """View for about."""
    print("Serving about to ", request.headers.get('X-FORWARDED-FOR', None))

    installed_version = os.environ.get('VERSION')
    if not installed_version:
        installed_version = 'dev'

    content = """
        <div class="row"><div class="col s12">
            <div class="card blue-grey darken-1"><div class="card-content white-text"><span class="card-title">About</span>
                <p>
                    This tool can help you manage your 'custom_components' for Home Assistant.</br>
                    This will <b>only</b> manage the '.py' files for you under 'custom_components/', </br>you still need to manually add/remove entries in 'configuration.yaml'.</br></br>
                    All components that are trackable with this has a "REPOSITORY" button, use that to verify the content before installing/upgrading.</br>
                    Do <b>not</b> install/upgrade something with this that you do not trust.</br></br>
                    <hr>
                    <div class="row" style="margin-bottom: 2px;">
                        <div class="col s5">Installed version:</div>
                        <div class="col s7">{installed_version}</div>
                    </div>
                    <div class="row" style="margin-bottom: 2px;">
                        <div class="col s12"><a href="https://github.com/ludeeus/custom-component-store" target="_blank" >Project @ GitHub</a></div>
                    </div>
                    <div class="row" style="margin-bottom: 2px;">
                        <div class="col s12"><a href="https://hub.docker.com/r/ludeeus/custom-component-store" target="_blank" >Project @ Docker hub</a></div>
                    </div>
                </p>
            </div></div>

            <div class="card blue-grey darken-1"><div class="card-content white-text"><span class="card-title">Custom Components</span>
                <p>
                    All the components/platforms that you can manage with this needs to be added to <a href="https://github.com/ludeeus/customjson" target="_blank" >customjson</a>, 
                    by default all components/platforms that folow the standard in the <a href="https://github.com/custom-components" target="_blank" >custom-component org. on GitHub</a> are managable, other components/platforms would need to be added to <a href="https://github.com/ludeeus/customjson" target="_blank" >customjson</a> before they can show up here.</br>
                    The platform structure needs to be as embedded platforms to be managed here.
                </p>
            </div></div>

            <div class="card blue-grey darken-1"><div class="card-content white-text"><span class="card-title">Notice</span>
                <p>
                    This project uses many recources to work:
                    </br><a href="https://github.com/ludeeus/customjson" target="_blank" >customjson</a>
                    </br><a href="https://fontawesome.com/" target="_blank" >Font Awesome</a>
                    </br><a href="http://fonts.googleapis.com/css?family=Roboto" target="_blank" >fonts.googleapis.com</a>
                    </br><a href="https://materializecss.com" target="_blank" >materialize</a>
                    </br><a href="https://aiohttp.readthedocs.io/en/stable/" target="_blank" >aiohttp</a>
                    </br><a href="https://github.com/just-containers/s6-overlay" target="_blank" >s6-overlay</a>
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
    """.format(installed_version=installed_version)

    html = base_html.TOP
    html += base_html.BASE.format(main=content)
    html += base_html.END
    return web.Response(body=html, content_type="text/html", charset="utf-8")


async def installed_components_view(request):
    """Default/Installed view."""
    print("Serving default/Installed view to ", request.headers.get('X-FORWARDED-FOR', None))
    components = await data.get_data()
    installed = {}
    not_trackable = {}
    content = ''

    for component in components:
        if components[component]['installed']:
            installed[component] = components[component]

    if not installed:
        for component in data.EXAMPLE:
            installed[component] = data.EXAMPLE[component]

    for component in installed:
        if not installed[component]['trackable']:
            not_trackable[component] = installed[component]
            continue
        update = ''
        warning = ''

        if not ['embedded']:
            style = 'float: right;'
            message = '<i class="fa fa-info" style="color: darkred;"></i>'
            tooltip = 'Not managable'
            warning = base_html.TOOLTIP.format(style=style, message=message,
                                               tooltip=tooltip)

        if data.migration_needed(component):
            style = 'float: right;'
            message = '<i class="fa fa-info" style="color: darkred;"></i>'
            tooltip = 'Migration needed'
            warning = base_html.TOOLTIP.format(style=style, message=message,
                                               tooltip=tooltip)

        if installed[component]['has_update']:
            update = '<i class="fa fa-arrow-circle-up">&nbsp;</i>'

        description = installed[component]['description']

        if description is not None and ':' in description:
            description = description.split(':')[-1]

        content += """
            <div class="row">
            <div class="col s12">
                <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                    <span class="card-title">{update}{component}{warning}</span>
                    <p>{description}</p>
                </div>
                <div class="card-action">
                    <a href="/component/{component}">More info</a>
                </div>
                </div>
            </div>
            </div>
        """.format(update=update, component=component,
                   description=description, warning=warning)

    style = 'float: right;'
    message = '<i class="fa fa-info" style="color: darkred;"></i>'
    tooltip = 'Could not find matching data about these'
    warning = base_html.TOOLTIP.format(style=style, message=message,
                                       tooltip=tooltip)

    if not_trackable:
        content += """
            <div class="row">
            <div class="col s12">
                <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                <span class="card-title">{warning}</span></a>
            """.format(warning=warning)

        for component in not_trackable:

            content += """
                    <li>{component} ({path})</li>
                """.format(component=component,
                           path=installed[component]['local_location'][1:])
        content += """
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
    print("Serving 'The Store' to ", request.headers.get('X-FORWARDED-FOR', None))
    components = await data.get_data()
    content = ''

    for component in components:
        if not components[component]['trackable']:
            continue
        if components[component]['has_update']:
            update = '<i class="fa fa-arrow-circle-up">&nbsp;</i>'
        else:
            update = ''
        description = components[component]['description']
        if description is not None and ':' in description:
            description = description.split(':')[-1]

        if not components[component]['embedded']:
            style = 'float: right;'
            message = '<i class="fa fa-info" style="color: darkred;"></i>'
            tooltip = 'Not managable'
            warning = base_html.TOOLTIP.format(style=style, message=message,
                                               tooltip=tooltip)
        else:
            warning = ''

        content += """
            <div class="row">
            <div class="col s12">
                <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                    <span class="card-title">{update}{component}{warning}</span>
                    <p>{description}</p>
                </div>
                <div class="card-action">
                    <a href="/component/{component}">More info</a>
                </div>
                </div>
            </div>
            </div>
        """.format(update=update, component=component,
                   description=description, warning=warning)

    html = base_html.TOP
    html += base_html.BASE.format(main=content)
    html += base_html.END
    return web.Response(body=html, content_type="text/html", charset="utf-8")


async def component_view(request):
    """View for single component."""
    component = request.match_info['component']
    print("Serving view for", component, "to", request.headers.get('X-FORWARDED-FOR', None))
    if component == 'sensor.example':
        components = data.EXAMPLE
    else:
        components = await data.get_data()

    if component in components:

        button = '<a href="{target}" {extra}>{text}</a>'

        authordata = components[component].get('author')
        attention = components[component].get('attention')
        embedded = components[component].get('embedded')
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

        modal = button.format(target='/component/'+component+'/install',
                              extra='', text='INSTALL')

        button1 = button.format(target='#',
                                extra=toast+' id=isntallbtn', text='INSTALL')

        button2 = button.format(target=repository, extra='target="_blank"',
                                text='REPOSITORY')

        button3 = ''

        published_version = "Published version: {}".format(published_version)

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

            modal = button.format(target='/component/'+component+'/update',
                                  extra=toast, text='UPDATE')

            button1 = button.format(target='#',
                                    extra=toast+' id=isntallbtn', text='UPDATE')

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

        if data.migration_needed(component) and attention is None:
            attention = """
                You have this installed with the old format.</br>
                You need to move (migrate) it to an embedded platform.
                </br></br>
                <p>Option 1: Change the location of the platform</br>
                from: 'custom_components/{domain}/{platform}.py'</br>
                to: 'custom_components/{platform}/{domain}.py'</br></br></p>
                """.format(domain=component.split('.')[0], platform=component.split('.')[1])

            if embedded:
                attention += """<p>Option 2: Delete the file and reinstall with this site.</p>
                    <p></br></br>Option 3: Click the "MIGRATE" button.</p>
                    """
                button2 = button.format(target=component+'/migrate', extra='',
                                        text='MIGRATE')
            button4 = ''

        if not embedded and attention is None:
            attention = """
                This can not be installed/used with this site yet.</br>
                The developer of this must first migrate it to an embedded platform.
                </br></br></br><p>{}</br></br>{}{}
                """.format(description, author, published_version)

        if attention:
            author = ''
            button1 = ''
            button3 = ''
            description = ''
            installed_version = ''
            published_version = ''
            update = ''
            attention = """<p class="attention">{}</p></br>""".format(attention)
        else:
            attention = ''

        if component == 'sensor.example':
            button1 = ''

        content = """
            <div class="row">
            <div class="col s12">
                <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                    <span class="card-title">{update}{component}</span>
                    {attention}
                    <p>
                    {description}</br>
                    {image}</br>
                    {more_info}
                    {author}
                    {installed_version}
                    {published_version}
                    </br>
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
                   button2=button2, button3=button3, button4=button4, attention=attention)

        if installed:
            instype = 'upgrade'
        else:
            instype = 'install'

        content += """
        <div id="InstallModal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <p>Do <b>not</b> {type} this unless you trust the source.</br>
            </br>
            Click the "REPOSITORY" to check out the source, before installing this.</p>
            This {type} will <b>not</b> change <i>anything</i> in your configuration, you still need to manually update that.</br></br>
            <div class="card-action">
                {button}
            </div>
        </div>

        </div>
        """.format(button=modal, type=instype)
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
    print("Installing/updating", component, "triggered by", request.headers.get('X-FORWARDED-FOR', None))
    comp_data = await data.get_data()
    embedded = comp_data[component].get('embedded')
    if embedded:
        localpath = PATH + comp_data[component]['embedded_path']
        remotepath = comp_data[component]['embedded_path_remote']

        if '.' in component:
            if not os.path.exists(PATH + '/custom_components/' + component.split('.')[1]):
                os.makedirs(PATH + '/custom_components/' + component.split('.')[1])

        if '__init__.py' in comp_data[component]['embedded_path']:
            if not os.path.exists(PATH + '/custom_components/' + component):
                os.makedirs(PATH + '/custom_components/' + component)

        with open(localpath, 'wb') as file:
            file.write(requests.get(remotepath).content)
        file.close()
    raise web.HTTPFound('/component/' + component)


async def uninstall_component(request):
    """Uninstall component"""
    component = request.match_info['component']
    print("Uninstalling", component, "triggered by", request.headers.get('X-FORWARDED-FOR', None))
    comp_data = await data.get_data()
    embedded = comp_data[component].get('embedded')
    if embedded:
        path = PATH + comp_data[component]['embedded_path']
    else:
        path = PATH + comp_data[component]['local_location']
    os.remove(path)
    raise web.HTTPFound('/component/' + component)


async def migrate_component(request):
    """Migrate component"""
    component = request.match_info['component']
    print("Migrating", component, "triggered by", request.headers.get('X-FORWARDED-FOR', None))
    comp_data = await data.get_data()
    old_path = PATH + comp_data[component]['local_location']
    new_path = PATH + comp_data[component]['embedded_path']
    print('From', old_path, 'to', new_path)
    if '.' in component:
        if not os.path.exists(PATH + '/custom_components/' + component.split('.')[1]):
            os.makedirs(PATH + '/custom_components/' + component.split('.')[1])
    os.rename(old_path, new_path)
    raise web.HTTPFound('/component/' + component)


if __name__ == "__main__":
    DIRECTORY = PATH + '/custom_components'
    VERSION_PATH = PATH + '/.HA_VERSION'
    VERSION = 0
    TARGET = 86

    if not os.path.exists(VERSION_PATH):
        print("Could not find Home Assistant configuration")

    elif not os.path.exists(PATH):
        print(PATH, "does not exist...")

    else:
        with open(VERSION_PATH) as version_file:
            VERSION = version_file.readlines()
            VERSION = int(VERSION[0].split('.')[1])

        if not os.path.exists(DIRECTORY):
            os.makedirs(DIRECTORY)

    if VERSION >= TARGET:
        APP = web.Application()
        APP.router.add_route('GET', r'/', installed_components_view)
        APP.router.add_route('GET', r'/store', the_store_view)
        APP.router.add_route('GET', r'/json', json)
        APP.router.add_route('GET', r'/about', about_view)
        APP.router.add_route('GET', r'/component/{component}', component_view)
        APP.router.add_route('GET', r'/component/{component}/install', install_component)
        APP.router.add_route('GET', r'/component/{component}/update', install_component)
        APP.router.add_route('GET', r'/component/{component}/uninstall', uninstall_component)
        APP.router.add_route('GET', r'/component/{component}/migrate', migrate_component)
        APP.router.add_route('GET', r'/component/{component}/json', json)
        web.run_app(APP, port=9999, print=None)
    else:
        print("You need Home Assistant version 0.86 or newer to use this.")
