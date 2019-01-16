"""View for about."""
from componentstore.const import VERSION
import componentstore.resources.html as load


async def view():
    """View for about."""

    installed_version = VERSION
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

    html = load.TOP
    html += load.BASE.format(main=content)
    html += load.END

    return html
