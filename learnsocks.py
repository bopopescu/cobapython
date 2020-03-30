import socks

def init_socks(proxy, timeout):
    '''init a socks proxy socket.'''
    map_to_type = {
        'v4':   socks.SOCKS4,
        'v5':   socks.SOCKS5,
        'http': socks.HTTP
    }
    ssock = socks.socksocket()
    if isinstance(timeout, (int, float)):
        ssock.settimeout(timeout)
    ssock.set_proxy(proxy_type=map_to_type[proxy.get('socks_type', 'v5')],
                    rdns=proxy.get('rdns', True),
                    addr=proxy.get('host'), 
                    port=proxy.get('port'), 
                    username=proxy.get('username'), 
                    password=proxy.get('password'))
    return ssock 

init_socks(proxy = "81.28.164.55",timeout = 52658)
