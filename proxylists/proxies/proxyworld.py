# https://www.freeproxy.world/


from .server import ProxyServer


class ProxyWorld(ProxyServer):
    url = "https://www.freeproxy.world/?country=US"
    table_attribute: str = 'layui-table'
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
            if i.xpath('.//td[6]//a[contains(text(),"http")]'):
                ip = i.xpath('.//td[1]/text()')[0].strip()
                port = i.xpath('.//td[2]//a/text()')[0].strip()
                proxy = ":".join(
                    [ip, port]
                )
                proxies.append(proxy)
        return proxies
