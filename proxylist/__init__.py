import asyncio
from .proxies import PROXY_LIST


async def proxy_list():
    proxies = []
    for proxy in PROXY_LIST:
        p = await proxy().get_list()
        proxies = proxies + p
    return proxies


def get_proxies():
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(proxy_list())
