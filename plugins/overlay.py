from twisted.python import log
import tempfile, subprocess, os

class Plugin:
    def __init__(self):
        log.msg("Loading plugin - overlay")
        self.applicationHeaders = ['application/octet-stream','application/x-msdos-program']

    def isFrakable(self, key, value):
        #is the header of type we want to frak with
        if key.lower() == 'content-type':
            for val in self.applicationHeaders:
                if value in val:
                    log.msg("Response is binary, INFECT! INFECT!...")
                    return True
        return False

    def frak(self, data):
	log.msg("Overlay!")
        #frak the data
	bfp = tempfile.NamedTemporaryFile()
        bfp.write(data)
        bfp.flush()
        	
        bfp.close()
        return data

