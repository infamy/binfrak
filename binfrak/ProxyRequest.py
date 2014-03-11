from twisted.web import http, proxy
import binfrak.ProxyClientFactory

class ProxyRequest(proxy.ProxyRequest):
    '''ProxyRequest class stub
    '''
    protocols = dict(http=binfrak.ProxyClientFactory)
