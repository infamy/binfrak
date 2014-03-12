from twisted.python import log
from twisted.web import http, proxy
import gzip, StringIO, binfrak

class ProxyClient(proxy.ProxyClient):
    """Where all the magic happens. This class is where we intercept the data."""

    def __init__(self, command, rest, version, headers, data, father):
        self.father = father
        self.command = command
        self.rest = rest
        self.data = ""
        if "proxy-connection" in headers:
            del headers["proxy-connection"]
        headers["connection"] = "close"
        self.headers = headers
        self.isCompressed = False
        self.contentLength = None
        self.plugin = None

    def handleResponcePart(self, data):
        self.data += data

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

    def handleResponseEnd(self):
        log.msg("Response handler")
        if self.isCompressed:
            log.msg("Decompressing")
            self.data = gzip.GzipFile('', 'rb', 9, StringIO.StringIO(self.data)).read()

        #log.msg( "Read from server:\n" + data)
        #frak with bin files here.
        if self.plugin:
            log.msg("Plugin running...")
            self.data = self.plugin.frak(self.data)

        #if self.contentLength != None:
        #    self.father.setHeader('Content-Length', len(data))

        self.father.transport.write(self.data)

    #def shutdown(self):
    #     self.father.transport.finish()
    #     self.father.transport.loseConnection()










