from twisted.python import log
import tempfile, subprocess, os, Image

class Plugin:
    def __init__(self):
        log.msg("Loading plugin - overlay")
        self.applicationHeaders = ['image/']

    def isFrakable(self, key, value):
        #is the header of type we want to frak with
        if key.lower() == 'content-type':
            for val in self.applicationHeaders:
                if val in value:
                    log.msg("Response is image, Ponies! Ponies!...")
                    return True
        return False

    def frak(self, data):
        log.msg("Overlay!")
        #frak the data
        bfp = tempfile.NamedTemporaryFile()
        bfp.write(data)
        bfp.flush()
        background = Image.open(bfp.name)
        foreground = Image.open("dt_small.png")
        background.paste(foreground, (0, 0), foreground)
        background.show()
        ifp = tempfile.NamedTemporaryFile()
        background.save(ifp.name,"png")
        data = ifp.read()
        ifp.close()
        bfp.close()
        return data

