"""View for 'The Store'."""
import store.resources.html as load
from store.functions.data import get_data

async def view():
    """View for 'The Store'."""

    components = await get_data()
    content = load.SEARCH

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
            warning = load.TOOLTIP.format(
                style=style, message=message, tooltip=tooltip)
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

    html = load.TOP
    html += load.BASE.format(main=content)
    html += load.END

    return html
