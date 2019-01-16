"""View for single component."""
import store.resources.html as load
from store.functions.data import get_data, migration_needed
from store.const import EXAMPLE


async def view(component):
    """View for single component."""

    if component == 'sensor.example':
        components = EXAMPLE
    else:
        components = await get_data()

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

        needs_migration = await migration_needed(component)

        if needs_migration and attention is None:
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

    html = load.TOP
    html += load.BASE.format(main=content)
    html += load.END

    return html
