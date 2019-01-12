"""Static texts."""
STYLE = """
<head>
    <title>Custom Components</title>
    <link rel="shortcut icon" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAAZiS0dEAAAAAAAA+UO7fwAAAAlwSFlzAAAASAAAAEgARslrPgAAAWNJREFUSMfl1btKXUEUBuAPGw1YKJhC0tqIEX0DU6Y44gG18CVsLSTY2oilBNKlSZN0FoLiC9jkCQRtRAQRRfR42SnO2mEY3O5zvIDgD8OePWut/5/bWsN7QgN/ozVekngUmyiytoPJ5xAP4wfuMuJFnET/NnyGuyH+gCWcPTDrInwGsYqrGLuI//468iYOK4hTgRIj+J3YDjBTRT6OmxryoiJ2ObHfYOwhp50OyOtWcBTfrZx8OiP5hvOaM1jDdYztYxaf0Iqxr6nAAu4zkk5u0UVsTx/mQqj0m89X0VuxDRPYzkTu8TNmPIHdzP6l6qAfO8hGYl/BEDa0c6HAcU18rUBqP8Zp9FtYx8BLCpRtG5+7iP/v0FNj/6V981L0dCJwGQ57mOpihVMRUwRHJZra6V4S/dFOpiqBkfBJS0VTDfJi18J3fEyInlzsUpSJVl7Dk0TgWeU6x6s9ODle7cl82/gH8SrATLXsQgIAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTktMDEtMTJUMjE6NTA6MjArMDA6MDAMfMVgAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE5LTAxLTEyVDIxOjUwOjIwKzAwOjAwfSF93AAAACh0RVh0c3ZnOmJhc2UtdXJpAGZpbGU6Ly8vdG1wL21hZ2ljay1sMWQ4YWhNNAMMbZUAAAAASUVORK5CYII=" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link href='http://fonts.googleapis.com/css?family=Roboto' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    <style>
       @media only screen and (max-device-width : 1024px) {
            main {
                width: 100%;
            }
        }
        body {
            padding-left: 5px !important;
            font-family: roboto !important;
            display: flex;
            min-height: 100vh;
            flex-direction: column;
        }
        main {
          flex: 1 0 auto;
          width: 50%;
          margin: auto;
        }
        .fa {
            font-size:18px !important;
        }
        code {
            font-family: roboto !important;
            font-size: 14px !important;
        }
        nav {
            background-color: #546e7a !important;
            margin-bottom: 32px;
        }
        .card-title {
            color: white;
        }
        footer {
            margin-right: 5px;
        }
        header {
            margin-right: 5px;
        }
        .uninstall {
          color: darkred !important;
          font-weight: bolder;
        }
    </style>
</head>
"""
HEADER = """
<header>
  <nav>
    <div class="nav-wrapper">
      <a href="#" class="brand-logo">&nbsp;&nbsp;&nbsp;Custom Components</a>
      <ul id="nav-mobile" class="right hide-on-med-and-down">
        <li><a href="/">Installed Components</a></li>
        <li><a href="/components">"The Store"</a></li>
      </ul>
    </div>
  </nav>
</header>
"""

CARD = """
  <div class="row">
    <div class="col s12">
      <div class="card blue-grey darken-1">
        <div class="card-content white-text" id="{comp}">
          <a href="#{comp}"><span class="card-title">{comp}</span></a>
          <p>{content}</p>
        </div>
        <div class="card-action">
          <a href="{target}">{button}</a>
          <a href="{repo}" target="_blank">Repository</a>
          {extra}
        </div>
      </div>
    </div>
  </div>
"""

FOOTER = """
<footer class="page-footer blue-grey darken-1">
  <div class="container" style="padding-bottom: 15px;;">
    <i>This site is not created, developed, affiliated, supported, maintained or endorsed by Home Assistant.</i>
  </div>
</footer>
"""

CONTENT = """
</br>
</br>
Installed version: {installed}</br>
Published version: {version}</br>
"""

EXTRA = """
<a href="{notes}" target="_blank">Release notes</a>
<a href="{uninstall}" class="uninstall">Uninstall</a>
"""

NOCOMPONENTS = """
  <div class="row">
    <div class="col s12">
      <div class="card blue-grey darken-1">
        <div class="card-content white-text">
          <span class="card-title">No components installed :(</span></a>
          <p>Go to "The store" abowe to get some awesome components.</p>
        </div>
      </div>
    </div>
  </div>
"""