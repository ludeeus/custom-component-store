"""Setup configuration."""
import setuptools


setuptools.setup(
    name="componentstore",
    version="1.0.0",
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
