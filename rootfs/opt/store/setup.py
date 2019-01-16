"""Setup configuration."""
import setuptools


setuptools.setup(
    name="store",
    version="0.0.0",
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    install_requires=['aiohttp', 'requests', 'click'],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'store = store.cli:cli'
        ]
    }
)
