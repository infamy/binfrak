from twisted.web import proxy
from binfrak.ProxyClient import ProxyClient

class ProxyClientFactory(proxy.ProxyClientFactory):
    '''ProxyClientFactory class stub'''
    protocol = ProxyClient
