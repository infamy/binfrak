from twisted.python import log
from twisted.web import http, proxy
import gzip, StringIO

class ProxyClient(proxy.ProxyClient):

    def handleHeader(self, key, value):
        # change response header here
        log.msg("Header: %s: %s" % (key, value))
        proxy.ProxyClient.handleHeader(self, key, value)
	
    def handleResponse(self, data):
        if (self.isCompressed):
            log.msg("Decompressing content...")
            data = gzip.GzipFile('', 'rb', 9, StringIO.StringIO(data)).read()
            
        #log.msg( "Read from server:\n" + data)

        if (self.contentLength != None):
            self.client.setHeader('Content-Length', len(data))
        
        self.client.write(data)
        self.shutdown()

class ProxyClientFactory(proxy.ProxyClientFactory):
    protocol = ProxyClient

class ProxyRequest(proxy.ProxyRequest):
    protocols = dict(http=ProxyClientFactory)

class Proxy(proxy.Proxy):
    requestFactory = ProxyRequest

class ProxyFactory(http.HTTPFactory):
    protocol = Proxy
	
listenport = 10000

if __name__ == '__main__':
    import sys
    from twisted.internet import reactor

    def shutdown(reason, reactor, stopping=[]):
        """Stop the reactor."""
        if stopping: return
        stopping.append(True)
        if reason:
            log.msg(reason.value)
        reactor.callWhenRunning(reactor.stop)

    log.startLogging(sys.stdout)
    reactor.listenTCP(int(listenport),ProxyFactory())
    reactor.run()