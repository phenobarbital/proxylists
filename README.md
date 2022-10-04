# proxylists

Proxylists is a simple tool for getting a list of proxy IPs from
free proxy servers using several providers.

## Supported Providers:

 * free-proxy-list.net
 * hidemy.name
 * proxydb.net

can retrieve a list of IPs by provider or from all of them
using the "get_proxies()" method.

### Download

The list can be tabulated (one proxy by line, to save on .txt, csv, etc)
or a python dictionary.

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
print(proxies)
```
### License ###

Proxylists is licensed under BSD license.
