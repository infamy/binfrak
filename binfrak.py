

listenport = 10000

if __name__ == '__main__':
    import sys
    from binfrak.ProxyFactory import ProxyFactory
    from twisted.internet import reactor
    from twisted.python import log

    def shutdown(reason, reactor, stopping=[]):
        """Stop the reactor."""
        if stopping:
            return
        stopping.append(True)
        if reason:
            log.msg(reason.value)
        reactor.callWhenRunning(reactor.stop)

    log.startLogging(sys.stdout)
    reactor.listenTCP(int(listenport), ProxyFactory())
    reactor.run()
