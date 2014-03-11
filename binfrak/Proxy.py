from twisted.web import proxy
import binfrak.ProxyRequest

class Proxy(proxy.Proxy):
    '''Proxy class stub
    '''
    requestFactory = binfrak.ProxyRequest
