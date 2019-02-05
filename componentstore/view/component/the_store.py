"""View for 'The Store'."""
import componentstore.resources.html as load
from componentstore.functions.data import get_data, migration_needed

async def view():
    """View for 'The Store'."""

    components = await get_data()
    content = load.RELOADICON.format('/reloadstore')
    content += load.SEARCHBAR

    for component in components:
        cardtitle = ''

        if not components[component]['trackable']:
            continue

        if components[component]['has_update']:
            cardtitle += load.UPDATEICON

        cardtitle += component

        needs_migration = await migration_needed(component)

        if needs_migration:
            cardtitle += load.TOOLTIP.format('Migration needed')

        elif not components[component]['embedded']:
            cardtitle += load.TOOLTIP.format('Not managable')

        cardcontent = load.META.format(
            type='author', text=components[component]['author']['login'])

        cardcontent += load.TEXT.format(components[component]['description'])
        cardbutton = load.LINK.format(
            url='/component/'+component, target='_self',
            style='', id='', htmlclass='', extra='', text='More info')

        content += load.BUTTON_CARD.format(
            title=cardtitle, content=cardcontent, buttons=cardbutton)

    html = load.TOP
    html += load.BASE.format(content)
    html += load.END

    return html
