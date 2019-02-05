"""View for about."""
from componentstore.const import VERSION, DEMO
import componentstore.resources.html as load


async def view():
    """View for about."""

    installed_version = VERSION
    if not installed_version:
        installed_version = 'dev'
    if DEMO:
        installed_version = installed_version + '(DEMO)'

#------------------------------------------------------------------------------

    about = load.TEXT.format(
        "This tool can help you manage your 'custom_components' for Home Assistant.")
    about += load.BREAK
    about += load.TEXT.format(
        "This will only manage the '.py' files for you under 'custom_components/', "
        "you still need to manually add/remove entries in 'configuration.yaml'.")
    about += load.BREAK
    about += load.TEXT.format(
        "All components that are trackable with this has a 'REPOSITORY' button, "
        "use that to verify the content before installing/upgrading.")
    about += load.BREAK
    about += load.TEXT.format(
        "Do not install/upgrade something with this that you do not trust.")
    about += load.HR

    lines = load.LINE.format(
        type='installed_version', text='installed version: '+installed_version)

    text = load.LINK.format(
        url='https://github.com/ludeeus/custom-component-store',
        target='_blank', style='', id='', htmlclass='', extra='',
        text='Project @ GitHub')
    lines += load.LINE.format(type='github_link', text=text)

    text = load.LINK.format(
        url='https://hub.docker.com/r/ludeeus/custom-component-store',
        target='_blank', style='', id='', htmlclass='', extra='',
        text='Project @ Docker hub')
    lines += load.LINE.format(type='docker_hub_link', text=text)

    about += load.LIST.format(title='', lines=lines)

    content = load.BASE_CARD.format(
        title='About', content=about)

#------------------------------------------------------------------------------

    customjson = load.LINK.format(
        url='https://github.com/ludeeus/customjson',
        target='_blank', style='', id='', htmlclass='', extra='',
        text='customjson')

    org = load.LINK.format(
        url='https://github.com/custom-components',
        target='_blank', style='', id='', htmlclass='', extra='',
        text='custom-component org. on GitHub')

    text = """
    All the components/platforms that you can manage with this needs to
    be added to {customjson}, by default all components/platforms that folow 
    the standard in the {org} are managable, other components/platforms would 
    need to be added to {customjson} before they can show up here.
    """.format(customjson=customjson, org=org)

    components = load.TEXT.format(text)
    components += load.TEXT.format(
        "The platform structure needs to be as embedded platforms to be managed here.")

    content += load.BASE_CARD.format(
        title='Custom Components', content=components)

#------------------------------------------------------------------------------

    notice = load.TEXT.format("This project uses many recources to work:")

    links = [
        {
            'link': 'https://github.com/ludeeus/customjson',
            'text': 'customjson'
        },
        {
            'link': 'https://fontawesome.com/',
            'text': 'Font Awesome'
        },
        {
            'link': 'http://fonts.googleapis.com/css?family=Roboto',
            'text': 'fonts.googleapis.com'
        },
        {
            'link': 'https://materializecss.com',
            'text': 'materialize'
        },
        {
            'link': 'https://aiohttp.readthedocs.io/en/stable/',
            'text': 'aiohttp'
        },
        {
            'link': 'https://github.com/just-containers/s6-overlay',
            'text': 's6-overlay'
        },
        {
            'link': 'https://redis.io/',
            'text': 'redis'
        }
    ]
    for link in links:
        notice += load.LINK.format(
            url=link['link'], target='_blank', style='', id='', htmlclass='',
            extra='', text=link['text'])
        notice += load.BREAK

    content += load.BASE_CARD.format(
        title='Notice', content=notice)

#------------------------------------------------------------------------------

    text = load.TEXT.format(
        "This is in the footer of every page here, but I think that it belongs here to.")
    text += load.BREAK
    text += load.TEXT.format(
        "This site and the items here is not created, developed, affiliated, "
        "supported, maintained or endorsed by Home Assistant.")

    content += load.NO_TITLE_CARD.format(text)

#------------------------------------------------------------------------------

    text = load.LINK.format(
        url='https://www.buymeacoffee.com/ludeeus', target='_blank', style='',
        id='', htmlclass='', extra='', text=load.COFFEEICON+'Buy me a coffee? :D')

    content += load.NO_TITLE_CARD.format(text)

#------------------------------------------------------------------------------

    html = load.TOP
    html += load.BASE.format(content)
    html += load.END

    return html
