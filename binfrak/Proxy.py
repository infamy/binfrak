from twisted.web import proxy
from binfrak.ProxyRequest import ProxyRequest

class Proxy(proxy.Proxy):
    '''Proxy class stub.'''
    requestFactory = ProxyRequest
