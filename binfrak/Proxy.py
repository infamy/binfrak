from twisted.web import proxy
import binfrak.ProxyRequest

class Proxy(proxy.Proxy):
    requestFactory = binfrak.ProxyRequest
