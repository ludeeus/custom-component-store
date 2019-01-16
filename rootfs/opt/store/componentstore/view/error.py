"""View for error."""
from componentstore.server import REASON
import componentstore.resources.html as load


async def view():
    """View for error."""

    if REASON == 'version':
        reason = "You need Home Assistant version 0.86 or newer to use this."
    elif REASON == 'no_path':
        reason = "Defined HA configuration path not found."
    elif REASON == 'ha_not_found':
        reason = "Home Assistant installation not found on the specified path."
    else:
        reason = "An unexpected error occurred."

    content = """
        <div class="row">
            <div class="col s12">
                <div class="card blue-grey darken-1">
                    <div class="card-content white-text">
                        <span class="card-title">Something went wrong</span>
                        <p>
                            {reason}</br></br>
                            code: {reasoncode}
                        </p>
                    </div>
                </div>
            </div>
        </div>
    """.format(reason=reason, reasoncode=REASON)

    html = load.TOP
    html += load.BASE.format(main=content)
    html += load.END

    return html
