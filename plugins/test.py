from twisted.python import log

class Plugin:
    def __init__(self):
        log.msg("Loading plugin - test")
        self.applicationHeaders = ['application/octet-stream']

    def isFrakable(self, key, value):
        #is the header of type we want to frak with
        if key.lower() == 'content-type':
            for val in self.applicationHeaders:
                if value in val:
                    log.msg("Response is binary, INFECT! INFECT!...")
                    return True
        return False

    def frak(self, data):
        #frak the data
        data += "THIS IS A TEST APPEND"
        return data
