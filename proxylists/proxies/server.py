from abc import abstractmethod
import aiohttp
from lxml.html import fromstring


class ProxyServer:
    url = ""
    parser = None

    async def get_list(self):
        timeout = aiohttp.ClientTimeout(total=60)
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Dnt": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/83.0.4103.97 Safari/537.36",
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, headers=headers, timeout=timeout) as response:
                if response.status == 200:
                    try:
                        content = await response.text()
                    except Exception as e:
                        print(e)
                        b = await response.content.read()
                        content = b.decode("utf-8")
                    self.parser = fromstring(content)
                    return await self.get_proxies()

    @abstractmethod
    async def get_proxies(self):
        pass

    async def get_proxy_list(self) -> dict:
        proxies = await self.get_list()
        return {
            'http': f'http://{proxies[0]}',
            'https': f'http://{proxies[0]}',
        }
