import asyncio

from .freeproxy import FreeProxy
from .proxydb import ProxyDB
from .hidemy import Hidemy

__all__ = ["FreeProxy", "Hidemy", "ProxyDB"]

PROXY_LIST = [ProxyDB, Hidemy, FreeProxy]
