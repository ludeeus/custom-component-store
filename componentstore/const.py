"""Constants"""
import os


PATH = os.environ.get('HA_CONFIG_PATH', '/config')

VERSION = '1.2.0'

REDIS_TOPIC_BASE = 'custom_component_store_'

DEMO = os.environ.get('DEMO')
DEMOTEXT = "This is a demo"

DOMAINS = ['sensor', 'switch', 'media_player', 'climate', 'light',
           'binary_sensor']

EXAMPLE = {
    "sensor.example": {
        "trackable": True,
        "embedded_path": "/custom_components/example/sensor.py",
        "version": VERSION,
        "installed": False,
        "imagelink": "https://images.pexels.com/photos/577585/pexels-photo-577585.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",  # pylint: disable=C0301
        "visit_repo": "https://github.com/ludeeus/custom-component-store",
        "embedded_path_remote": "https://github.com/ludeeus/custom-component-store",
        "changelog": "https://github.com/ludeeus/custom-component-store",
        "embedded": True,
        "has_update": False,
        "local_location": "/custom_components/sensor/example.py",
        "local_version": VERSION,
        "author": {
            "login": "ludeeus",
            "html_url": "https://github.com/ludeeus"
        },
        "description": "Example sensor entity.",
        "remote_location": "https://github.com/ludeeus/custom-component-store"
    }
}
