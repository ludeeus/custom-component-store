# custom-component-store

![overview][image_link]

This tool can help you manage your `custom_components` for Home Assistant.  
This will only manage the `.py` files for you under `custom_components/`, 
you still need to manually add/remove entries in `configuration.yaml`.

Only components/platforms the are generated with [`customjson`][customjson] can be managed.

Platforms can **only** be managed if they the remote repository are using the new embedded structure that was introduced in 0.86.0

**Home Assistant version 0.86 or newer is required to use this.**

## Installation on Docker (Recomended)

```bash
docker run -d \
  --name custom-component-store \
  -p 8100:8100 \
  -v /path/to/HA/config:/config \
  -e USERNAME=YOURUSERNAME \
  -e PASSWORD=YOURPASSWORD \
  ludeeus/custom-component-store:latest
```

`/path/to/HA/config` **must** be the root of your Home Assistant configuration, and this **has** to be `rw`.

If you use `hass.io` this will be `/usr/share/hassio/homeassistant`. You can also install the Hass.io Addon instead of the vanilla Docker container.

When the container is running point your browser to `http://HOST:8100`

ENV | Type | Description
-- | -- | --
USERNAME | String | Username for HTTP Basic Auth
PASSWORD | String | Password for HTTP Basic Auth

***

**You still get to use this if you are not running Home Assistant in docker, but that is the easiest way to get started.**

## Installation on Hass.io
### Hass.io Addon (simple)
A [Hass.io addon][addon] made by [@antoni-k][antonik] exists.

### Old method (advanced)
It's possible to use the regular Docker container on Hass.io as well.

If you use the generic `hass.io` installer, use the instructions for docker.

If you use HassOS use the [Community SSH][ssh_addon] or [Portainer][portainer_addon] add-ons to run the docker container.

## Manual installation

```bash
python3 -m pip install componentstore
```

Then run as the user running HA:

```bash
componentstore --nocache --username USERNAME --password PASSWORD
```

## Demo

[DEMO][demo]
![gif][gif_link]

## Notice

This is not created, developed, affiliated, supported, maintained or endorsed by Home Assistant.

[antonik]: https://github.com/antoni-k
[addon]: https://github.com/antoni-k/hassio-addons/tree/master/custom-component-store
[ssh_addon]: https://github.com/hassio-addons/addon-ssh
[portainer_addon]: https://github.com/hassio-addons/addon-portainer
[image_link]: https://i.ibb.co/my9BJNK/image.png
[gif_link]: https://i.ibb.co/BszqLXr/demo.gif
[customjson]: https://github.com/ludeeus/customjson
[demo]: https://componentstoredemo.halfdecent.io/
[pythonfiles]: https://github.com/ludeeus/custom-component-store/tree/master/rootfs/opt/store/componentstore
[nginx]: https://www.nginx.com/
[redis]: https://redis.io/
[data]: https://github.com/ludeeus/data/blob/master/custom-component-store/V1/data.json
[pypi]: https://pypi.org/project/componentstore/

***

[![BuyMeCoffee](https://camo.githubusercontent.com/cd005dca0ef55d7725912ec03a936d3a7c8de5b5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6275792532306d6525323061253230636f666665652d646f6e6174652d79656c6c6f772e737667)](https://www.buymeacoffee.com/ludeeus)