"""Tests.

Testing get_proxies.
"""
import pytest
import asyncio
from datetime import datetime
import timeit
from proxylist import get_proxies, proxy_list


pytestmark = pytest.mark.asyncio


@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


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
        pass # TODO: checking if is a valid -reachable- proxy
