binfrak
=======

Plugins
Writing plugins will allow you to extend binfrak to allow you to frak with the data, be it a binary, js, html, images. A plugin is a simple class that is required to have 

def isFrakable(self, key, value):
	#if you want frak to be run for this by its header#
		return True
	else
		return False

def frak(self, data):
	#frak with the data
	return data


