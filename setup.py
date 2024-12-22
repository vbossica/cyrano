import os
from setuptools import setup

setup(
    name="cyrano",
    version=os.environ.get("MODULE_VERSION", "0.0.1"),
    author='Vladimir Ritz Bossicard',
    author_email='vbossica@gmail.com',
    url='https://github.com/vbossica/cyrano',
    description='Cyrano',
    long_description='Cyrano',
    download_url='https://github.com/vbossica/cyrano',
    license='UNLICENSED',
    package_dir={'cyrano': 'cyrano'},
    install_requires=[
        'knack >= 0.12.0',
    ],
    entry_points={
        'console_scripts': [
            'cyrano=cyrano.__main__:main'
        ]
    }
)
