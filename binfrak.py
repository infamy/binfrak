import os
import sys
from twisted.python import log
from binfrak.ProxyFactory import ProxyFactory
from twisted.internet import reactor

path = "plugins/"
plugins = {}

def shutdown(reason, reactor, stopping=[]):
    """Stop the reactor."""
    if stopping:
        return
    stopping.append(True)
    if reason:
        log.msg(reason.value)
    reactor.callWhenRunning(reactor.stop)

def main():
    log.startLogging(sys.stdout)
    log.msg("Loading Plugins")

    # Load plugins
    sys.path.insert(0, path)
    for f in os.listdir(path):
        fname, ext = os.path.splitext(f)
        if ext == '.py':
            mod = __import__(fname)
            plugins[fname] = mod.Plugin()
    sys.path.pop(0)

    listenport = 10000

    reactor.listenTCP(int(listenport), ProxyFactory())
    reactor.run()

if __name__ == '__main__':
    main()

