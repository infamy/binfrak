from twisted.python import log
from twisted.web import http, proxy
import gzip, StringIO

class ProxyClient(proxy.ProxyClient):

    def __init__(self, command, uri, postData, headers, client):
        self.isCompressed = False
        self.contentLength = None

    def handleHeader(self, key, value):
        # change response header here
        log.msg("Header: %s: %s" % (key, value))

        if key.lower() == 'content-encoding':
            if value.find('gzip') != -1:
                logging.debug("Response is compressed...")
                self.isCompressed = True

        if key.lower() == 'content-length':
            self.contentLength = value

        proxy.ProxyClient.handleHeader(self, key, value)

    def handleResponse(self, data):
        if self.isCompressed:
            log.msg("Decompressing content...")
            data = gzip.GzipFile('', 'rb', 9, StringIO.StringIO(data)).read()

        #log.msg( "Read from server:\n" + data)
	#frak with bin files here.

        if self.contentLength != None:
            self.client.setHeader('Content-Length', len(data))

        self.client.write(data)
        self.shutdown()










