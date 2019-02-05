"""Base HTML"""
from componentstore.resources.style import STYLE
from componentstore.const import DEMO, DEMOTEXT


TITLE = "Custom Components"

if DEMO:
    TITLE = "{} - {}".format(TITLE, DEMOTEXT)


SCRIPT = """
$(document).ready(function(){
  $("#componentsearch").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("main .row").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
"""

TOP = """
<head>
    <title>{title}</title>
    <link rel="shortcut icon" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAAZiS0dEAAAAAAAA+UO7fwAAAAlwSFlzAAAASAAAAEgARslrPgAAAWNJREFUSMfl1btKXUEUBuAPGw1YKJhC0tqIEX0DU6Y44gG18CVsLSTY2oilBNKlSZN0FoLiC9jkCQRtRAQRRfR42SnO2mEY3O5zvIDgD8OePWut/5/bWsN7QgN/ozVekngUmyiytoPJ5xAP4wfuMuJFnET/NnyGuyH+gCWcPTDrInwGsYqrGLuI//468iYOK4hTgRIj+J3YDjBTRT6OmxryoiJ2ObHfYOwhp50OyOtWcBTfrZx8OiP5hvOaM1jDdYztYxaf0Iqxr6nAAu4zkk5u0UVsTx/mQqj0m89X0VuxDRPYzkTu8TNmPIHdzP6l6qAfO8hGYl/BEDa0c6HAcU18rUBqP8Zp9FtYx8BLCpRtG5+7iP/v0FNj/6V981L0dCJwGQ57mOpihVMRUwRHJZra6V4S/dFOpiqBkfBJS0VTDfJi18J3fEyInlzsUpSJVl7Dk0TgWeU6x6s9ODle7cl82/gH8SrATLXsQgIAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTktMDEtMTJUMjE6NTA6MjArMDA6MDAMfMVgAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE5LTAxLTEyVDIxOjUwOjIwKzAwOjAwfSF93AAAACh0RVh0c3ZnOmJhc2UtdXJpAGZpbGU6Ly8vdG1wL21hZ2ljay1sMWQ4YWhNNAMMbZUAAAAASUVORK5CYII=" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link href='http://fonts.googleapis.com/css?family=Roboto' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script>
    {script}
    </script>
    <style>
    {style}
    </style>
</head>
<body>
<header style="padding-bottom: 2.5%;">
  <div class="navbar-fixed">
    <nav>
      <div class="nav-wrapper">
        <a href="/" class="brand-logo">&nbsp;&nbsp;&nbsp;{title}</a>
        <ul id="nav-mobile" class="right hide-on-med-and-down">
          <li><a href="/">Installed</a></li>
          <li><a href="/store">"The Store"</a></li>
          <li><a href="/about">About</a></li>
        </ul>
      </div>
    </nav>
  </div>
</header>
""".format(title=TITLE, script=SCRIPT, style=STYLE)


BASE = """
<main>
{}
</main>
"""


END = """
  <footer class="page-footer blue-grey darken-1">
    <div class="container" style="padding-bottom: 15px;">
      <i>This site and the items here is not created, developed, affiliated, supported, maintained or endorsed by Home Assistant.</i>
    </div>
  </footer>
</body>
"""


TOOLTIP = """
<div class="tooltip" style="float: right;">
  <i class="fa fa-info" style="color: darkred;"></i>
  <span class="tooltiptext">{}</span>
</div>
"""


SEARCHBAR = """
<input id="componentsearch"
type="text"
placeholder="Search.."
style="width: 95%;margin-left: 2.5%;margin-bottom: 2.5%;margin-top: -2.5%;"
autofocus>
"""


LINK = """
<a href="{url}" target="{target}" class="{htmlclass}" style="{style}" id="{id}" {extra}>{text}</a>
"""

IMAGE = """
<img src="{}"</a>
"""

TOAST = """
onclick="M.toast({html: 'MESSAGE', displayLength: 10000})"
"""


ATTENTION = """
<span class="attention">{}</span></br>
"""


TEXT = """
<p class="text">{}</p>
"""

META = """
<p name="{type}" style="display: none;">{text}</p>
"""


BASE_CARD = """
<div class="row">
  <div class="col s12">
    <div class="card blue-grey darken-1">
      <div class="card-content white-text">
        <span class="card-title">{title}</span>
        {content}
      </div>
    </div>
  </div>
</div>
"""


BUTTON_CARD = """
<div class="row">
  <div class="col s12">
    <div class="card blue-grey darken-1">
      <div class="card-content white-text">
        <span class="card-title">{title}</span>
        {content}
      </div>
      <div class="card-action">
        {buttons}
      </div>
    </div>
  </div>
</div>
"""


NO_TITLE_CARD = """
<div class="row">
  <div class="col s12">
    <div class="card blue-grey darken-1">
      <div class="card-content white-text">
        {}
      </div>
    </div>
  </div>
</div>
"""


MODAL_SCRIPT = """
<script>
var modal = document.getElementById('InstallModal');
var btn = document.getElementById("installbtn");
var span = document.getElementsByClassName("close")[0];
btn.onclick = function() {
  modal.style.display = "block";
}
span.onclick = function() {
  modal.style.display = "none";
}
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
var modal = document.getElementById('InstallModal');
var btn = document.getElementById("uninstallbtn");
var span = document.getElementsByClassName("close")[0];
btn.onclick = function() {
  modal.style.display = "block";
}
span.onclick = function() {
  modal.style.display = "none";
}
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
</script>
"""


MODAL = """
<div id="InstallModal" class="modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <p>Do <b>not</b> {type} this unless you trust the source.
    </br></br>
    Click the "REPOSITORY" to check out the source, before installing this.</p>
    This {type} will <b>not</b> change <i>anything</i> in your configuration, 
    you still need to manually update that.</br></br>
    <div class="card-action">
        <a href="/component/{component}/{type}">{text}</a>
    </div>
</div>
</div>
"""


DEMO_MODAL = """
<div id="InstallModal" class="modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <p>This is a demo</p>
    <p>install, upgrade, migrate and uninstall has been disabled.</p>
</div>
</div>
"""


UPDATEICON = """
<div class="tooltip" style"background-color: #546e7ad4;">
  <i class="fa fa-arrow-circle-up">&nbsp;</i>
  <span class="tooltiptext">Update pening</span>
</div>
"""

RELOADICON = """
<a href="{}">
  <i class="fa fa-repeat reload">&nbsp;</i>
</a>
"""

COFFEEICON = '<i class="fa fa-coffee">&nbsp;</i>'
LINE = '<li id={type}>{text}</li>'
BREAK = '</br>'
HR = '<hr>'


LIST = """
<div class="row">
  <div class="col s12">
    <div class="card blue-grey darken-1">
      <div class="card-content white-text">
        <span class="card-title">{title}</span></a>
        {lines}
      </div>
    </div>
  </div>
</div>
"""


CARD_MENU = """
  <div class="card-dropdown">
    <i class="fa fa-ellipsis-v"></i>
    <div class="card-dropdown-content">
      <a href="{repo}/issues/" target="_blank">Open a issue</a>
      <a href="https://github.com/ludeeus/custom-component-store/issues/new?title={component}&labels=flag&assignee=ludeeus&template=flag.md" target="_blank">Flag this</a>
    </div>
  </div> 
"""
