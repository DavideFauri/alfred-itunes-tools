from xml.etree.ElementTree import ElementTree as ET
from os.path import expanduser


# 1 - find the main xml file
# 2 - check for a .bak file, create it if absent
# 3 - parse for playlists, use key/value dicts with names as keys
# 4 - 







home = expanduser("~")
srcfile = home + "/Music/iTunes/iTunes Music Library.xml"

tree = ET().parse(srcfile)

tree.find('.')

playlists = tree.findall('./dict/array/dict')
print(playlists[0].attrib)

#playlists = tree.findall('./dict/array/dict/string')
#print(list(n.text for n in playlists if "dumb" in n.text))