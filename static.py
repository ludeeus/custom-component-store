"""Static texts."""
STYLE = """
<head>
    <title>Custom Components</title>
    <link rel="shortcut icon" href="data:image/x-icon;base64,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" />
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