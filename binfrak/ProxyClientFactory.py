from twisted.web import proxy
import binfrak.ProxyClient

class ProxyClientFactory(proxy.ProxyClientFactory):
    protocol = binfrak.ProxyClient
