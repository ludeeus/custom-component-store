# custom-component-store

![overview][image_link]

This tool can help you manage your `custom_components` for Home Assistant.  
This will only manage the `.py` files for you under `custom_components/`, 
you still need to manually add/remove entries in `configuration.yaml`.

Only components/platforms the are generated with [`customjson`][customjson] can be managed.

Platforms can **only** be managed if they the remote repository are using the new embedded structure that was introduced in 0.86.0

**Home Assistant version 0.86 or newer is required to use this.**

## Installation on Docker

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

if you use `hass.io` this will be `/usr/share/hassio/homeassistant`.

When the container is running point your browser to `http://DOCKERHOST:8100`

ENV | Type | Description
-- | -- | --
USERNAME | String | Username for HTTP Basic Auth
PASSWORD | String | Password for HTTP Basic Auth

***

You get still use this if you are not running Home Assistant in docker, but that is the easies way to get started.

### `Hass.io`

If you use the generic `hass.io` installer, use the instructions for docker.

If you use HassOS use the [Community SSH][ssh_addon] or [Portainer][portainer_addon] add-ons to run the docker container.

## Why docker container?

This is a bundle that contains 3 parts to operate:

- [The webserver (python)][pythonfiles]
- [Nginx for authentication][nginx]
- [redis for caching of data][redis]

## Demo

[DEMO][demo]
![gif][gif_link]

## Notice

This is not created, developed, affiliated, supported, maintained or endorsed by Home Assistant.

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