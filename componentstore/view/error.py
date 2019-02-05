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
    elif REASON == 'redis_conn_error':
        reason = "There was en error connecting to redis."
    else:
        reason = "An unexpected error occurred."

    cardcontent = load.TEXT.format(reason)
    cardcontent += load.BREAK
    cardcontent += load.BREAK
    cardcontent = load.TEXT.format('code: '+REASON)

    content = load.BASE_CARD.format(
        title='Something went wrong', content=cardcontent)

    html = load.TOP
    html += load.BASE.format(content)
    html += load.END

    return html
