import os
import sys
from twisted.python import log
from binfrak.ProxyFactory import ProxyFactory
from twisted.internet import reactor

def main():
    log.startLogging(sys.stdout)    

    listenport = 10000

    reactor.listenTCP(int(listenport), ProxyFactory())
    reactor.run()

if __name__ == '__main__':
    main()

