"""Tests.

Testing get_proxies.
"""
import pytest
import asyncio
from datetime import datetime
import timeit
from proxylists import get_proxies, proxy_list, check_address
import pytest_asyncio
from proxylists.proxies import ProxyDB  # getting from proxydb.net


pytestmark = pytest.mark.asyncio


async def test_proxylist(event_loop):
    """ Test Proxy List"""
    error = None
    proxies = []
    try:
        proxies = await proxy_list()
        print(proxies)
    except Exception as err:
        print(err)
        error = err
    pytest.assume(len(proxies) > 0)
    pytest.assume(not error)
    tasks = []
    for proxy in proxies:
        pass  # TODO: checking if is a valid -reachable- proxy


async def test_proxy(event_loop):
    try:
        list = await ProxyDB().get_list()
        print(list)
        for address in list:
            try:
                host, port = address.split(':')
                print('HOST: ', host, port)
                reachable = await check_address(
                    host=host,
                    port=port
                )
                print(host, port, reachable)
                pytest.assume(reachable is True)
                await asyncio.sleep(1)
            except Exception as err:
                print(err)
                pytest.assume(not err)
    finally:
        pytest.assume(len(list) > 0)
