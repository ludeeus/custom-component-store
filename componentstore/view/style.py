"""Style"""

STYLE = """
<style>
    @media (max-device-width : 1024px) main {
            width: 100%;
        }
    nav .brand-logo {
        left: 0px;
        -webkit-transform: none;
        transform: none;
        }
    .hide-on-med-and-down {
        display: unset !important;
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
      width: 60%;
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
    .uninstall {
      color: darkred !important;
      font-weight: bolder;
      float: right;
    }
    .container {
        width: 95% !important;
    }
    .attention {
      color: darkred !important;
      font-weight: bolder;
    }
    img.overview {
        max-width: 95%;
    }
    .author {
        color: #ffab40;
    }
    a {
        color: #ffab40;
    }
    .tooltip {
        position: relative;
        display: inline-block;
    }
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 250px;
        background-color: #546e7aa1;
        text-align: center;
        border-radius: 6px;
        padding: 5px 0;

        /* Position the tooltip */
        position: absolute;
        z-index: 1;
        font-size: small;
    }
    .tooltip:hover .tooltiptext {
        visibility: visible;
    }

    .modal {
        display: none; /* Hidden by default */
        position: fixed; /* Stay in place */
        z-index: 1; /* Sit on top */
        padding-top: 100px; /* Location of the box */
        left: 0;
        top: 0;
        width: 100%; /* Full width */
        height: 100%; /* Full height */
        overflow: auto; /* Enable scroll if needed */
        background-color: rgba(0, 0, 0, 0.01); /* Black w/ opacity */
        -webkit-box-shadow: none;
        box-shadow: none;
    }

    /* Modal Content */
    .modal-content {
        background-color: #546e7af2;
        color: #fff;
        margin: auto;
        padding: 20px;
        border: 1px solid #888;
        width: 50%;
        margin-top: 100px;
    }

    /* The Close Button */
    .close {
    color: #aaaaaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
    }

    .close:hover,
    .close:focus {
        color: #000;
        text-decoration: none;
        cursor: pointer;
    }
    html {
        overflow: scroll;
        overflow-x: hidden;
    }
    ::-webkit-scrollbar {
        width: 0px;  /* remove scrollbar space */
        background: transparent;  /* optional: just make scrollbar invisible */
    }
    /* optional: show position indicator in red */
    ::-webkit-scrollbar-thumb {
        background: #FF0000;
    }
</style>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
"""
