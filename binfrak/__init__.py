import sys, os

def loadPlugins():
    path = "plugins/"
    plugins = {}
    sys.path.insert(0, path)
    for f in os.listdir(path):
        fname, ext = os.path.splitext(f)
        if ext == '.py':
            mod = __import__(fname)
            plugins[fname] = mod.Plugin()
    sys.path.pop(0)
    #disable plugins
    #plugins = {}
    return plugins
