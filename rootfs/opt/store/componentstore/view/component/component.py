"""View for single component."""
import componentstore.resources.html as load
from componentstore.functions.data import get_data, migration_needed
from componentstore.const import EXAMPLE, DEMO


async def view(component):
    """View for single component."""

    content = load.RELOADICON.format('/reloadinstalled')

    data = await component_data(component)

    meta = {}
    meta['attention'] = data.get('attention')
    meta['author'] = ''
    meta['cardbuttons'] = ''
    meta['cardcontent'] = ''
    meta['cardtitle'] = ''
    meta['name'] = component
    meta['description'] = data.get('description')
    meta['long_description'] = data.get('long_description')
    meta['image'] = ''
    meta['install_or_upgrade'] = 'install'
    meta['update'] = ''
    meta['warning'] = ''

    if data:
        buttons = {}
        buttons['1'] = ''
        buttons['2'] = ''
        buttons['3'] = ''
        buttons['4'] = ''
        buttons['5'] = ''
        buttons['6'] = ''

        if data['installed']:
            buttons['1'] = load.LINK.format(
                url='/component/'+meta['name'], target='_self',
                style='', id='1', htmlclass='', extra='',
                text='CHECK FOR UPDATE')

            buttons['6'] = load.LINK.format(
                url='/component/'+meta['name']+'/uninstall', target='_self',
                style='', id='4', htmlclass='uninstall', extra='',
                text='UNINSTALL')

        else:
            buttons['1'] = load.LINK.format(
                url='#', target='_self',
                style='', id='installbtn', htmlclass='', extra='',
                text=meta['install_or_upgrade'])

        if data['has_update']:
            meta['cardtitle'] += load.UPDATEICON
            meta['install_or_upgrade'] = 'upgrade'
            buttons['1'] = load.LINK.format(
                url='#', target='_self',
                style='', id='installbtn', htmlclass='', extra='',
                text=meta['install_or_upgrade'])
            buttons['4'] = load.LINK.format(
                url=data['changelog'], target='_blank',
                style='', id='3', htmlclass='', extra='', text='CHANGELOG')

        if data.get('author'):
            link = load.LINK.format(
                url=data['author'].get('html_url'), target='_blank',
                style='', id='3', htmlclass='', extra='',
                text='@'+data['author'].get('login'))
            meta['author'] = load.TEXT.format('Author: '+link)

        buttons['3'] = load.LINK.format(
            url=data['visit_repo'], target='_blank',
            style='', id='2', htmlclass='', extra='', text='REPOSITORY')

        meta['cardtitle'] += meta['name']
        meta['cardtitle'] += load.CARD_MENU.format(
            repo=data['visit_repo'], component=meta['name'])

        needs_migration = await migration_needed(component)

        if needs_migration:
            meta['warning'] = load.TOOLTIP.format('Migration needed')
            domain = component.split('.')[0]
            platform = component.split('.')[1]

            meta['attention'] = "You have this installed with the old format."
            meta['attention'] += load.BREAK
            meta['attention'] += "You need to move (migrate) it to an embedded platform."
            meta['attention'] += load.BREAK
            meta['attention'] += load.BREAK
            option1 = "Option 1: Change the location of the platform"
            option1 += load.BREAK
            option1 += "from: custom_components/{domain}/{platform}.py".format(
                domain=domain, platform=platform)
            option1 += load.BREAK
            option1 += "to: 'custom_components/{platform}/{domain}.py'".format(
                domain=domain, platform=platform)
            option1 += load.BREAK
            meta['attention'] += load.TEXT.format(option1)

            if data['embedded']:
                meta['attention'] += load.TEXT.format(
                    "Option 2: Delete the file and reinstall with this site.")
                meta['attention'] += load.BREAK
                meta['attention'] += load.TEXT.format(
                    "Option 3: Click the 'MIGRATE' button.")

                if DEMO:
                    buttons['2'] = load.LINK.format(
                        url='#', target='_self', style='', id='installbtn',
                        htmlclass='', extra='', text='MIGRATE')
                else:
                    buttons['2'] = load.LINK.format(
                        url='/component/'+component+'/migrate', target='_self',
                        style='', id='2', htmlclass='', extra='',
                        text='MIGRATE')

        if not data['embedded']:
            meta['attention'] = "This can not be installed/used with this site yet."
            meta['attention'] += load.BREAK
            meta['attention'] += "The developer of this must first migrate "
            meta['attention'] += "it to an embedded platform."

        if meta['attention']:
            buttons['1'] = ''
            buttons['4'] = ''
            meta['attention'] = load.ATTENTION.format(meta['attention'])
        else:
            meta['attention'] = ''

        if meta['description']:
            meta['cardcontent'] += load.TEXT.format(meta['description'])
            meta['cardcontent'] += load.BREAK

        if meta['attention']:
            meta['cardcontent'] += meta['attention']
            meta['cardcontent'] += load.BREAK

        if data['image_link']:
            meta['image'] = load.IMAGE.format(data['image_link'])
            meta['cardcontent'] += meta['image']
            meta['cardcontent'] += load.BREAK
            meta['cardcontent'] += load.BREAK

        if meta['long_description']:
            meta['cardcontent'] += load.TEXT.format(meta['long_description'])
            meta['cardcontent'] += load.BREAK

        if meta['author']:
            meta['cardcontent'] += load.TEXT.format(meta['author'])

        if data['local_version']:
            text = "Installed version: {}".format(data['local_version'])
            meta['cardcontent'] += load.TEXT.format(text)

        if data['version']:
            text = "Published version: {}".format(data['version'])
            meta['cardcontent'] += load.TEXT.format(text)

        if component == 'sensor.example':
            buttons['1'] = ''

        if DEMO and data['installed']:
            buttons['6'] = load.LINK.format(
                url='#', target='_self',
                style='', id='uninstallbtn', htmlclass='uninstall', extra='',
                text='uninstall')

        meta['cardbuttons'] += buttons['1']
        meta['cardbuttons'] += buttons['2']
        meta['cardbuttons'] += buttons['3']
        meta['cardbuttons'] += buttons['4']
        meta['cardbuttons'] += buttons['5']
        meta['cardbuttons'] += buttons['6']

        content += load.BUTTON_CARD.format(
            title=meta['cardtitle'],
            content=meta['cardcontent'],
            buttons=meta['cardbuttons'])

        if DEMO:
            content += load.DEMO_MODAL
        else:
            content += load.MODAL.format(
                component=meta['name'], type=meta['install_or_upgrade'],
                text=meta['install_or_upgrade'].upper())
        content += load.MODAL_SCRIPT
    else:
        content = load.NO_TITLE_CARD.format(
            'Component '+meta['name']+' not found')

    html = load.TOP
    html += load.BASE.format(content)
    html += load.END

    return html


async def component_data(component):
    """Return component data."""
    data = {}
    if component == 'sensor.example':
        component = EXAMPLE['sensor.example']
    else:
        component = await get_data(component=component)
    try:
        data['author'] = component.get('author')
        data['attention'] = component.get('attention')
        data['embedded'] = component.get('embedded')
        data['changelog'] = component.get('changelog')
        data['description'] = component.get('description')
        data['long_description'] = component.get('long_description')
        data['has_update'] = component.get('has_update')
        data['image_link'] = component.get('image_link')
        data['installed'] = component.get('installed')
        data['local_version'] = component.get('local_version')
        data['version'] = component.get('version')
        data['visit_repo'] = component.get('visit_repo')
    except Exception:  # pylint: disable=W0703
        pass
    return data
