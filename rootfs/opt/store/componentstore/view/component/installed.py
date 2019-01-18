"""Default/Installed view."""
from componentstore.functions.data import get_data, migration_needed
from componentstore.const import EXAMPLE
import componentstore.resources.html as load


async def view():
    """Default/Installed view."""
    components = await get_data()
    installed = {}
    not_trackable = {}
    content = load.RELOADICON.format('/reloadinstalled')
    content += load.SEARCHBAR

    for component in components:
        if components[component]['installed']:
            installed[component] = components[component]

    if not installed:
        installed = EXAMPLE

    for component in installed:
        if not installed[component]['trackable']:
            not_trackable[component] = installed[component]
            continue

        cardtitle = ''

        if installed[component]['has_update']:
            cardtitle += load.UPDATEICON

        cardtitle += component

        needs_migration = await migration_needed(component)

        if needs_migration:
            cardtitle += load.TOOLTIP.format('Migration needed')

        elif not installed[component]['embedded']:
            cardtitle += load.TOOLTIP.format('Not managable')

        cardcontent = load.META.format(
            type='author', text=installed[component]['author']['login'])

        cardcontent += load.TEXT.format(installed[component]['description'])

        cardbutton = load.LINK.format(
            url='/component/'+component, target='_self',
            style='', id='', htmlclass='', extra='', text='More info')

        content += load.BUTTON_CARD.format(
            title=cardtitle, content=cardcontent, buttons=cardbutton)

    if not_trackable:
        lines = ''
        warning = load.TOOLTIP.format(
            'Could not find matching data about these')

        for component in not_trackable:
            text = "{component} ({path})".format(
                component=component,
                path=installed[component]['local_location'][1:])

            lines += load.LINE.format(type='not_trackable', text=text)

        content += load.LIST.format(title=warning, lines=lines)

    html = load.TOP
    html += load.BASE.format(content)
    html += load.END

    return html
