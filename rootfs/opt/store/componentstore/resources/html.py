"""Base HTML"""
#from style import STYLE
from componentstore.resources.style import STYLE


TOP = """
<head>
    <title>Custom Components</title>
    <link rel="shortcut icon" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAAZiS0dEAAAAAAAA+UO7fwAAAAlwSFlzAAAASAAAAEgARslrPgAAAWNJREFUSMfl1btKXUEUBuAPGw1YKJhC0tqIEX0DU6Y44gG18CVsLSTY2oilBNKlSZN0FoLiC9jkCQRtRAQRRfR42SnO2mEY3O5zvIDgD8OePWut/5/bWsN7QgN/ozVekngUmyiytoPJ5xAP4wfuMuJFnET/NnyGuyH+gCWcPTDrInwGsYqrGLuI//468iYOK4hTgRIj+J3YDjBTRT6OmxryoiJ2ObHfYOwhp50OyOtWcBTfrZx8OiP5hvOaM1jDdYztYxaf0Iqxr6nAAu4zkk5u0UVsTx/mQqj0m89X0VuxDRPYzkTu8TNmPIHdzP6l6qAfO8hGYl/BEDa0c6HAcU18rUBqP8Zp9FtYx8BLCpRtG5+7iP/v0FNj/6V981L0dCJwGQ57mOpihVMRUwRHJZra6V4S/dFOpiqBkfBJS0VTDfJi18J3fEyInlzsUpSJVl7Dk0TgWeU6x6s9ODle7cl82/gH8SrATLXsQgIAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTktMDEtMTJUMjE6NTA6MjArMDA6MDAMfMVgAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE5LTAxLTEyVDIxOjUwOjIwKzAwOjAwfSF93AAAACh0RVh0c3ZnOmJhc2UtdXJpAGZpbGU6Ly8vdG1wL21hZ2ljay1sMWQ4YWhNNAMMbZUAAAAASUVORK5CYII=" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link href='http://fonts.googleapis.com/css?family=Roboto' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <style>
    {style}
    </style>
</head>
<body>
<header style="padding-bottom: 2.5%;">
  <div class="navbar-fixed">
    <nav>
      <div class="nav-wrapper">
        <a href="/" class="brand-logo">&nbsp;&nbsp;&nbsp;Custom Components</a>
        <ul id="nav-mobile" class="right hide-on-med-and-down">
          <li><a href="/">Installed</a></li>
          <li><a href="/store">"The Store"</a></li>
          <li><a href="/about">About</a></li>
        </ul>
      </div>
    </nav>
  </div>
</header>
""".format(style=STYLE)


BASE = """
<main>
{main}
</main>
"""


END = """
<footer class="page-footer blue-grey darken-1">
  <div class="container" style="padding-bottom: 15px;">
    <i>This site and the items here is not created, developed, affiliated, supported, maintained or endorsed by Home Assistant.</i>
  </div>
</footer>
<script>
  var modal = document.getElementById('InstallModal');
  var btn = document.getElementById("isntallbtn");
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
<script>
$(document).ready(function(){
  $("#componentsearch").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("main .row").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
</script>
</body>
"""

TOOLTIP = """
  <div class="tooltip" style="{style}">
      {message}
      <span class="tooltiptext">{tooltip}</span>
  </div>
"""

SEARCH = """
<input id="componentsearch" type="text" placeholder="Search.." 
style="width: 95%;margin-left: 2.5%;margin-bottom: 2.5%;margin-top: -2.5%;"
autofocus>
"""
