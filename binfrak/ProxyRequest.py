from twisted.web import http, proxy
from binfrak.ProxyClientFactory import ProxyClientFactory

class ProxyRequest(proxy.ProxyRequest):
    '''ProxyRequest class stub'''
    protocols = dict(http=ProxyClientFactory)
