"""
Geonode Proxy information.
"""
import os
from requests.models import PreparedRequest
import aiohttp
from .server import ProxyServer

class Geonode(ProxyServer):
    """
    Get Proxy From Geonode.
    """
    geonode_dns = None
    base_url: str = 'http://{username}:{password}@{geonode_dns}'

    def __init__(self, **kwargs):
        self.username = kwargs.get(
            'username',
            os.environ.get('GEONODE_USERNAME')
        )
        self.password = kwargs.get(
            'password',
            os.environ.get('GEONODE_PASSWORD')
        )
        self.geonode_dns: int = kwargs.get(
            'geonode_dns',
            os.environ.get(
                'GEONODE_DNS',
                'premium-residential.geonode.com:9000'
            )
        )
        self.country: str = kwargs.get('country', 'US')
        user = f"{self.username}-country-{self.country.upper()}"
        self.proxy_url = self.base_url.format(
            username=user,
            password=self.password,
            country=self.country,
            geonode_dns=self.geonode_dns,
        )

    async def get_list(self):
        proxies = []
        proxies.append(self.proxy_url)
        return proxies


class GeonodeFree(ProxyServer):
    """
    Get Proxy From Geonode using Free List.
    """
    base_url: str = 'https://proxylist.geonode.com/api/proxy-list'

    def __init__(self, **kwargs):
        args = {
            "limit": kwargs.get('limit', 20),
            "page": 1,
            "sort_by": "lastChecked",
            "sort_type": "desc"
        }
        http_only = kwargs.get('http_only', False)
        if http_only:
            args['protocols'] = 'http'
        req = PreparedRequest()
        req.prepare_url(self.base_url, args)
        self.url = req.url

    async def get_proxies(self):
        proxies = []
        timeout = aiohttp.ClientTimeout(total=10)
        async with aiohttp.ClientSession(
            timeout=timeout,
            trust_env=True
        ) as session:
            try:
                async with session.get(
                    self.url
                ) as response:
                    content = await response.json()
                    for proxy in content['data']:
                        print('PROXY ', proxy, '\n')
                        if proxy.get('latency') < 250:
                            for protocol in proxy.get('protocols'):
                                proxies.append(
                                    f"{protocol}://{proxy['ip']}:{proxy['port']}"
                                )
            except aiohttp.ClientProxyConnectionError as e:
                print(f"Proxy connection error: {e}")
            except aiohttp.ClientHttpProxyError as e:
                print(f"Request timed out: {e}")
            except aiohttp.ClientError as e:
                print(f"Client error occurred: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            except Exception as e:
                print(f'Proxy error: {e}')
        return proxies
