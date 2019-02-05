"""Setup configuration."""
import setuptools
from componentstore.const import VERSION


setuptools.setup(
    name="componentstore",
    version=VERSION,
    author="Joakim Sorensen",
    author_email="ludeeus@gmail.com",
    description="",
    long_description="",
    url="https://github.com/ludeeus/custom-component-store",
    long_description_content_type="text/markdown",
    install_requires=['aiohttp', 'requests', 'click', 'redis',
                      'aiohttp-basicauth'],
    packages=setuptools.find_packages(),
    package_data={'': ['./static/*']},
    entry_points={
        'console_scripts': [
            'componentstore = componentstore.cli:cli'
        ]
    }
)
