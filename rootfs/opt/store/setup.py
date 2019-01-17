"""Setup configuration."""
import setuptools
from componentstore.const import VERSION


setuptools.setup(
    name="componentstore",
    version=VERSION,
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    install_requires=['aiohttp', 'requests', 'click'],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'componentstore = componentstore.cli:cli'
        ]
    }
)
