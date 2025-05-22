"""
Get Free Proxies using Spyis Service.
"""
import logging
from .server import ProxyServer


class SpysOne(ProxyServer):
    """
    Get Free Proxies using Spyis Service.
    """
    url: str = 'https://spys.one/free-proxy-list/US/'

    async def get_proxies(self):
        proxies = []
        try:
            table = self.parser.xpath("//table")[1]
        except Exception as err:
            logging.exception(err)
            return
