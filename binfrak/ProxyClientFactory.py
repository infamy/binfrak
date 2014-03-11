from twisted.web import proxy
import binfrak.ProxyClient

class ProxyClientFactory(proxy.ProxyClientFactory):
    '''ProxyClientFactory class stub
    '''
    protocol = binfrak.ProxyClient
