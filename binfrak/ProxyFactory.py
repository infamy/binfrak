from twisted.web import http
import binfrak.Proxy

class ProxyFactory(http.HTTPFactory):
    protocol = binfrak.Proxy
