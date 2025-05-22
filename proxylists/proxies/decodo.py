"""
Decodo Proxy information.
"""
import os
import random
import logging
import aiohttp
from .server import ProxyServer

class Decodo(ProxyServer):
    """
    Decodo Proxy information.
    """
    https_support: bool = True
    url_base: str = '{country}.decodo.com'
    url: str = "{username}:{password}@{url_base}:{port}"

    def __init__(self, **kwargs):
        self.username = kwargs.get(
            'username',
            os.environ.get('DECODO_USERNAME')
        )
        self.password = kwargs.get(
            'password',
            os.environ.get('DECODO_PASSWORD')
        )
        self.country: str = kwargs.get('country', 'gate')
        url_base = self.url_base.format(
            country=self.country
        )
        # get a port number between 10001 and 10010
        self.port = kwargs.get('port', None) or random.choice(
            range(10001, 10011)
        )
        if self.port < 10001 or self.port > 10010:
            raise ValueError('Port must be between 10001 and 10010')
        self.customer_url = self.url.format(
            url_base=url_base,
            port=self.port,
            username=self.username,
            password=self.password,
            country=self.country,
        )
        self.customer = f"http://{self.customer_url}"
        self.proxy = {
            'http': f'http://{self.customer_url}',
            'https': f'https://{self.customer_url}',
        }

    async def get_list(self):
        return [self.customer]

    async def get_proxies(self):
        return self.proxy

    async def check_proxy(self):
        proxies = []
        timeout = aiohttp.ClientTimeout(total=self.timeout)
        async with aiohttp.ClientSession(
            timeout=timeout,
            trust_env=True
        ) as session:
            try:
                async with session.get(
                    url='https://ip.decodo.com/json',
                    proxy=self.proxy.get('http'),
                    allow_redirects=True
                ) as response:
                    content = await response.json()
                    proxies.append(content.get('proxy', {}).get('ip', None))
            except aiohttp.ClientProxyConnectionError as e:
                print(f"Proxy connection error: {e}")
            except aiohttp.ClientHttpProxyError as e:
                print(f"Request timed out: {e}")
            except aiohttp.ClientError as e:
                print(f"Client error occurred: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            except Exception as e:
                logging.error(f'Proxy error: {e}')
        return proxies
