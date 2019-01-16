# custom-component-store

**NOTE!: This is in an "alpha" stage, do NOT try to use this unless you know what you are doing, this should not be used or shared.**

![overview](https://i.ibb.co/BszqLXr/demo.gif)

This tool can help you manage your `custom_components` for Home Assistant.  
This will only manage the `.py` files for you under `custom_components/`, 
you still need to manually add/remove entries in `configuration.yaml`.

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

When the container is running point your browser to `http://DOCKERHOST:8100`

ENV | Type | Description
-- | -- | --
USERNAME | String | Username for HTTPBasicAuth
PASSWORD | String | Password for HTTPBasicAuth

***

You get still use this if you are not running Home Assistant in docker, but that is the easies way to get started.

### Hassio

If you use the generic hassio installer, use the instructions for docker.

If you use HassOS use the [Community SSH add-on](https://github.com/hassio-addons/addon-ssh) to run these.

### Other

**NB!: This method will not have authentication!**

**Python version 3.5.3+ is required.**

1. Install `customcomponentstore` with pip
1. Run `customcomponentstore`

## Notice

This is not created, developed, affiliated, supported, maintained or endorsed by Home Assistant.
