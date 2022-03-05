#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='dlocal',
    version='1.0.0',
    author='Preki',
    author_email='mariana@preki.com',
    packages=['dlocal', 'dlocal.models', 'dlocal.utils'],
    url='https://preki.com',
    download_url='https://github.com/GoPreki/DlocalSDK',
    license='MIT',
    description='Python library for handling Dlocal integration',
    long_description='Python library for handling Dlocal integration',
    install_requires=[
        'requests==2.27.0',
    ],
)
