import asyncio
from proxylists.proxies import ProxyWorld


async def proxy_list():
    proxies = await ProxyWorld().get_list()
    for p in proxies:
        print(p)
    return proxies


def get_proxies():
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(proxy_list())


if __name__ == "__main__":
    get_proxies()
