from .server import ProxyServer


class FreeProxy(ProxyServer):
    url = "https://free-proxy-list.net/"

    async def get_proxies(self):
        proxies = []
        table = self.parser.xpath('//table[@class="table table-striped table-bordered"]')[0]
        for i in table.xpath("//tbody/tr")[:10]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join(
                    [i.xpath(".//td[1]/text()")[0], i.xpath(".//td[2]/text()")[0]]
                )
                proxies.append(proxy)
        return proxies
