from twisted.web import http
from binfrak.Proxy import Proxy

class ProxyFactory(http.HTTPFactory):
    '''ProxyFactory class stub'''
    protocol = Proxy
