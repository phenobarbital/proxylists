import logging
from .server import ProxyServer


class ProxyDB(ProxyServer):
    url = "http://proxydb.net/?protocol=https&country="

    async def get_proxies(self):
        proxies = []
        try:
            table = self.parser.xpath("//table")[0]
        except Exception as err:
            logging.exception(err)
            return []
        for i in table.xpath("//tbody/tr")[:10]:
            if i.xpath('.//td[5][contains(text(),"HTTPS")]'):
                proxy = str(i.xpath(".//td[1]/a/text()")[0])
                proxies.append(proxy)
        return proxies
