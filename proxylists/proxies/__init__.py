import asyncio

from .freeproxy import FreeProxy
from .proxydb import ProxyDB
from .hidemy import Hidemy
from .proxyworld import ProxyWorld
from .oxylabs import Oxylabs
from .smart import SmartProxy
from .geonode import Geonode, GeonodeFree

__all__ = ["FreeProxy", "Hidemy", "ProxyDB"]

PROXY_LIST = [ProxyDB, Hidemy, FreeProxy]
