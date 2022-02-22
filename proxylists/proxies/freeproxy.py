from .server import ProxyServer


class FreeProxy(ProxyServer):
    url = "https://free-proxy-list.net/"
    table_attribute: str = 'table table-striped table-bordered'
    table_param: str = 'class'

    async def get_proxies(self):
        proxies = []
        try:
            path = f'//table[@{self.table_param}="{self.table_attribute}"]'
            table = self.parser.xpath(path)[0]
        except IndexError as err:
            print(err)
            return []
        for i in table.xpath("//tbody/tr")[:10]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join(
                    [i.xpath(".//td[1]/text()")[0], i.xpath(".//td[2]/text()")[0]]
                )
                proxies.append(proxy)
        return proxies
