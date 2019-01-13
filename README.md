# custom-component-store

![overview](https://i.ibb.co/BszqLXr/demo.gif)

## Installation

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

When the container is running point your browser to `http://DOCKERHOST:8100`

ENV | Type | Description
-- | -- | --
USERNAME | String | Username for HTTPBasicAuth
PASSWORD | String | Password for HTTPBasicAuth
NO_AUTH | Bool | Disable HTTPBasicAuth, you should **NEVER** set this to `true`.

***
## Notice

Inspiration on how to make this container comes from https://github.com/hassio-addons

The Community Hass.io add-ons for Home Assistant was created by [Franck Nijhof @frenck](https://github.com/frenck)
