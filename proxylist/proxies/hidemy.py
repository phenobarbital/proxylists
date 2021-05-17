from .server import ProxyServer


class Hidemy(ProxyServer):
    url = "https://hidemy.name/es/proxy-list/?type=s#list"

    async def get_proxies(self):
        proxies = []
        table = self.parser.xpath("//table")[0]
        for i in table.xpath("//tbody/tr")[:10]:
            if i.xpath('.//td[5][contains(text(),"HTTPS")]'):
                proxy = ":".join(
                    [i.xpath(".//td[1]/text()")[0], i.xpath(".//td[2]/text()")[0]]
                )
                proxies.append(proxy)
        return proxies
