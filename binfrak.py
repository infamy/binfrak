import os
import sys
from twisted.python import log
from binfrak.ProxyFactory import ProxyFactory
from twisted.internet import reactor

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

    listenport = 10000

    reactor.listenTCP(int(listenport), ProxyFactory())
    reactor.run()

if __name__ == '__main__':
    main()

