import socket
import asyncio


def check_host(host: str, port: int = 80, timeout: int = 2) -> bool:
    """
    Check if an Address is reachable and available.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(timeout)  # timeout
        s.connect((host, port))
        return True
    except Exception:
        return False
    finally:
        s.shutdown(socket.SHUT_RDWR)
        s.close()


async def check_address(host: str, port: int = 80, timeout: int = 2) -> bool:
    """
    Async version of test if an address (IP) is reachable.
    Parameters:
      host: str
        host IP address or hostname
      port : int
        HTTP port number
    Returns
    -------
    awaitable bool
    """
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(host, port),
            timeout=timeout
        )
        writer.close()
        await writer.wait_closed()
        return True
    except Exception:
        return False
