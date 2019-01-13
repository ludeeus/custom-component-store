"""Style"""

STYLE = """
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
        font-size:20px !important;
        color: #ffab40;
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
      float: right;
    }
    img.overview {
        max-width: 95%;
    }
</style>
"""
