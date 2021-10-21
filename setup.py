#!/usr/bin/env python
"""ProxyLists.

    Get a list of free Proxy Servers
See:
https://github.com/phenobarbital/proxylist
"""

from setuptools import setup, find_packages

setup(
    name='proxylists',
    version=open("VERSION").read().strip(),
    python_requires=">=3.7.0",
    url='https://github.com/phenobarbital/proxylist',
    description='List of Proxy Servers',
    long_description='Get a list of free Proxy Servers',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.8',
    ],
    author='Jesus Lara',
    author_email='jlara@trocglobal.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    setup_requires=[
        "wheel==0.37.0",
        "Cython==0.29.21",
        "asyncio==3.4.3",
        "cchardet==2.1.7"
    ],
    install_requires=[
        "wheel==0.37.0",
        "requests>=2.26.0",
        "aiohttp==3.7.4",
        "asyncio==3.4.3",
        "lxml==4.6.3",
        "uvloop>=0.16.0",
        'rapidjson>=1.0.0',
        'python-rapidjson>=1.5',
        'cchardet>=2.1.7'
    ],
    tests_require=[
            'pytest>=5.4.0',
            'coverage',
            'pytest-asyncio==0.14.0',
            'pytest-xdist==2.1.0',
            'pytest-assume==2.4.2'
    ],
    project_urls={  # Optional
        'Source': 'https://github.com/phenobarbital/proxylist',
        'Funding': 'https://paypal.me/phenobarbital',
        'Say Thanks!': 'https://saythanks.io/to/phenobarbital',
    },
)
