"""
Oxylabs Proxy information.
"""
import os
import logging
import aiohttp
from .server import ProxyServer

class Oxylabs(ProxyServer):
    """
    Oxylabs Proxy information.
    """
    https_support: bool = True
    oxylabs_base: str = 'pr.oxylabs.io:7777'
    url = 'customer-{username}-cc-{country}-sesstime-{ses_time}:{password}@{oxy}'

    def __init__(self, **kwargs):
        self.username = kwargs.get(
            'username',
            os.environ.get('OXYLABS_USERNAME')
        )
        self.password = kwargs.get(
            'password',
            os.environ.get('OXYLABS_PASSWORD')
        )
        self.country: str = kwargs.get('country', 'us')
        self.timeout: int = kwargs.get('timeout', 30.0)
        self.session_time: int = kwargs.get('session_time', 5)
        self.customer = self.url.format(
            username=self.username,
            password=self.password,
            ses_time=self.session_time,
            country=self.country,
            oxy=self.oxylabs_base
        )
        self.proxy = {
            'http': f'http://{self.customer}',
            'https': f'https://{self.customer}',
        }

    async def get_list(self):
        proxies = []
        proxies.append(self.customer)
        return proxies

    async def get_proxies(self):
        proxies = []
        timeout = aiohttp.ClientTimeout(total=self.timeout)
        async with aiohttp.ClientSession(
            timeout=timeout,
            trust_env=True
        ) as session:
            try:
                async with session.get(
                    'https://ip.oxylabs.io/location',
                    proxy=self.proxy.get('http'),
                    allow_redirects=True
                ) as response:
                    content = await response.json()
                    proxies.append(content['ip'])
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
