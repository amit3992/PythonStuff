import os
import urllib.request

curDir = os.getcwd()
print (curDir)

x = urllib.request.urlopen('https://www.google.com')

