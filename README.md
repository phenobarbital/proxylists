# proxylist

Get a list of free proxy servers from different providers

## Supported Providers:

 * free-proxy-list.net
 * hidemy.name
 * proxydb.net

can retrieve the list by provider or from all of them using the "get_proxies()" method.

### Download

The list can be tabulated (one proxy by line, to save on .txt, csv, etc) or a dictionary.

## Usage

```python

from proxylist import get_proxies

proxies = get_proxies()

```

Or get the list from a single provider:

```python

from proxylist.proxies import ProxyDB # getting from proxydb.net
import asyncio

async def get_proxies():
     return await ProxyDB().get_list()

loop = asyncio.get_event_loop()
proxies = loop.run_until_complete(get_proxies())
```
