#!/usr/bin/env python
import urlopen from urllib.request
import socket
import re


#opening remote objects using urllib
#import urlopen from urllib.request
webpage = urlopen('http://www.python.org') # or soecify a local file path
text = webpage.read()
m = re.search(b'<a href="([^"]+)" .*?>about</a>', text, re.IGNORECASE)
m.group(1)
#retrieving/ downloading the webpage
# urlretrieve('http://www.python.org', '"/home/fel/Pydev/python_web_page_download.html')
