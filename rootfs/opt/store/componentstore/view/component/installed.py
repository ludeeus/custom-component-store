"""Default/Installed view."""
from componentstore.functions.data import get_data, migration_needed
from componentstore.const import EXAMPLE
import componentstore.resources.html as load


async def view():
    """Default/Installed view."""
    components = await get_data()
    installed = {}
    not_trackable = {}
    content = load.SEARCH

    for component in components:
        if components[component]['installed']:
            installed[component] = components[component]

    if not installed:
        for component in EXAMPLE:
            installed[component] = EXAMPLE[component]

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
            warning = load.TOOLTIP.format(
                style=style, message=message, tooltip=tooltip)

        needs_migration = await migration_needed(component)

        if needs_migration:
            style = 'float: right;'
            message = '<i class="fa fa-info" style="color: darkred;"></i>'
            tooltip = 'Migration needed'
            warning = load.TOOLTIP.format(
                style=style, message=message, tooltip=tooltip)

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
    warning = load.TOOLTIP.format(
        style=style, message=message, tooltip=tooltip)

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
    html = load.TOP
    html += load.BASE.format(main=content)
    html += load.END

    return html
