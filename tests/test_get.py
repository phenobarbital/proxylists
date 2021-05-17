"""Tests.

Testing get_proxies.
"""
import pytest
import asyncio
from datetime import datetime
import timeit
from proxylists import get_proxies

@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()

async def test_proxylist(event_loop):
    """ Test Proxy List"""
    error = None
    try:
        proxies = get_proxies()
    except Exception as err:
        error = err
    pytest.assume(len(proxies) > 0)
    pytest.assume(not error)
    tasks = []
    for proxy in proxies:
        pass # TODO: checking if is a valid -reachable- proxy
