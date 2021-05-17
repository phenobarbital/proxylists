import requests
import aiohttp
import asyncio
from abc import abstractmethod

from lxml.html import fromstring


class ProxyServer(object):
    url = ''
    parser = None

    async def get_list(self):
        timeout = aiohttp.ClientTimeout(total=60)
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Dnt': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/83.0.4103.97 Safari/537.36'
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, headers=headers) as response:
                if response.status == 200:
                    try:
                        content = await response.text()
                    except Exception as e:
                        print(e)
                        b = await response.content.read()
                        content = b.decode('utf-8')
                    self.parser = fromstring(content)
                    return await self.get_proxies()

    @abstractmethod
    async def get_proxies(self):
        pass


class FreeProxy(ProxyServer):
    url = 'https://free-proxy-list.net/'

    async def get_proxies(self):
        proxies = set()
        table = self.parser.xpath('//table[@id="proxylisttable"]')[0]
        for i in table.xpath('//tbody/tr')[:10]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
        return proxies

class Hidemy(ProxyServer):
    url = 'https://hidemy.name/es/proxy-list/?type=s#list'

    async def get_proxies(self):
        proxies = set()
        table = self.parser.xpath('//table')[0]
        for i in table.xpath('//tbody/tr')[:10]:
            if i.xpath('.//td[5][contains(text(),"HTTPS")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
        return proxies

class ProxyDB(ProxyServer):
    url = 'http://proxydb.net/?protocol=https&country='

    async def get_proxies(self):
        proxies = set()
        table = self.parser.xpath('//table')[0]
        for i in table.xpath('//tbody/tr')[:10]:
            if i.xpath('.//td[5][contains(text(),"HTTPS")]'):
                proxy = i.xpath('.//td[1]/a/text()')[0]
                proxies.add(proxy)
        return proxies

PROXY_LIST = [ProxyDB, Hidemy, FreeProxy]

async def proxy_list():
    proxies = []
    for proxy in PROXY_LIST:
        p = await proxy().get_list()
        proxies.append(p)
    return proxies

def get_proxies():
    proxies = set()
    loop = asyncio.get_event_loop()
    proxies = loop.run_until_complete(proxy_list())
    return proxies
