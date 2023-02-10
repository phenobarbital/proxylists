"""ProxyLists.

    Get a list of free Proxy Servers
See:
https://github.com/phenobarbital/proxylists
"""
import ast
from os import path
from setuptools import setup, find_packages

def get_path(filename):
    return path.join(path.dirname(path.abspath(__file__)), filename)


def readme():
    with open(get_path('README.md'), encoding='utf-8') as rd:
        return rd.read()


version = get_path('proxylists/version.py')
with open(version, 'r', encoding='utf-8') as meta:
    # exec(meta.read())
    t = compile(meta.read(), version, 'exec', ast.PyCF_ONLY_AST)
    for node in (n for n in t.body if isinstance(n, ast.Assign)):
        if len(node.targets) == 1:
            name = node.targets[0]
            if isinstance(name, ast.Name) and \
                    name.id in (
                        '__version__',
                        '__title__',
                        '__description__',
                        '__author__',
                        '__license__', '__author_email__'):
                v = node.value
                if name.id == '__version__':
                    __version__ = v.s
                if name.id == '__title__':
                    __title__ = v.s
                if name.id == '__description__':
                    __description__ = v.s
                if name.id == '__license__':
                    __license__ = v.s
                if name.id == '__author__':
                    __author__ = v.s
                if name.id == '__author_email__':
                    __author_email__ = v.s


setup(
    name='proxylists',
    version=__version__,
    python_requires=">=3.8.0",
    url='https://github.com/phenobarbital/proxylists',
    description=__description__,
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    license=__license__,
    license_file='LICENSE',
    setup_requires=[
        "asyncio==3.4.3"
    ],
    install_requires=[
        "asyncio==3.4.3",
        "uvloop>=0.16.0",
        "aiohttp==3.8.3",
        'requests>=2.25.0',
        'requests[socks]>=2.25.1',
        'orjson==3.8.5',
        'lxml==4.9.2'
    ],
    tests_require=[
            'pytest>=5.4.0',
            'coverage'
    ],
    project_urls={  # Optional
        'Source': 'https://github.com/phenobarbital/proxylists',
        'Funding': 'https://paypal.me/phenobarbital',
        'Say Thanks!': 'https://saythanks.io/to/phenobarbital',
    },
)
