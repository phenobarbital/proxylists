"""
SmartProxy Proxy information.
"""
import os
from .server import ProxyServer

class SmartProxy(ProxyServer):
    """
    SmartProxy Proxy information.
    """
    base_url: str = 'http://{username}:{password}@{country}.smartproxy.com:{port}'

    def __init__(self, **kwargs):
        self.username = kwargs.get(
            'username',
            os.environ.get('SMARTPROXY_USERNAME')
        )
        self.password = kwargs.get(
            'password',
            os.environ.get('SMARTPROXY_PASSWORD')
        )
        self.port: int = kwargs.get(
            'port',
            os.environ.get('SMARTPROXY_PORT', 10001)
        )
        self.country: str = kwargs.get('country', 'us')
        user = f"{self.username}-country-{self.country}"
        self.proxy_url = self.base_url.format(
            username=user,
            password=self.password,
            country=self.country,
            port=self.port,
        )

    async def get_list(self):
        proxies = []
        proxies.append(self.proxy_url)
        return proxies
