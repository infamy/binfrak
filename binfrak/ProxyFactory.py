from twisted.web import http
import binfrak.Proxy

class ProxyFactory(http.HTTPFactory):
    '''ProxyFactory class stub'''
    protocol = binfrak.Proxy
