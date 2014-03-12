from twisted.python import log
from twisted.web import http, proxy
import gzip, StringIO, binfrak

class ProxyClient(proxy.ProxyClient):
    """Where all the magic happens. This class is where we intercept the data."""

    def __init__(self, command, rest, version, headers, data, father):
        self.father = father
	self.client = father
        self.command = command
        self.rest = rest
        self.headers = headers
        self.data = data
        self.isCompressed = False
        self.contentLength = None
        self.plugin = None

    def handleHeader(self, key, value):
        # change response header here
        log.msg("Header: %s: %s" % (key, value))
        plugins = binfrak.loadPlugins()
        if key.lower() == 'content-encoding':
            if value.find('gzip') != -1:
                log.msg("Response is compressed...")
                self.isCompressed = True

        if key.lower() == 'content-length':
            self.contentLength = value
	    log.msg(key, value)
        if self.plugin == None:
            for plugin in plugins.values():
                if plugin.isFrakable(key, value):
                    self.plugin = plugin
                    log.msg("Using:", plugin)

        proxy.ProxyClient.handleHeader(self, key, value)

    def handleResponsePart(self, data):
	log.msg("Response handler")
        if self.isCompressed:
            log.msg("compressed skipping")
            #self.client.write(data)
            #self.shutdown()
            #return
            #data = gzip.GzipFile('', 'rb', 9, StringIO.StringIO(data)).read()

        #log.msg( "Read from server:\n" + data)
        #frak with bin files here.
        if self.plugin and not self.isCompressed:
	    log.msg("Plugin running...")
            data = self.plugin.frak(data)

        if self.contentLength != None:
            self.client.setHeader('Content-Length', len(data))

        self.client.write(data)
        #self.shutdown()

    def shutdown(self):
         self.client.finish()
         self.transport.loseConnection()










