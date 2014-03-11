from twisted.web import http, proxy
import binfrak.ProxyClientFactory

class ProxyRequest(proxy.ProxyRequest):
    protocols = dict(http=binfrak.ProxyClientFactory)
