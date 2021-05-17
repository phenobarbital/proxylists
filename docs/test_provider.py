from proxylist.proxies import ProxyDB # getting from proxydb.net
import asyncio

async def get_proxies():
    return await ProxyDB().get_list()

loop = asyncio.get_event_loop()
proxies = loop.run_until_complete(get_proxies())
print(proxies)
