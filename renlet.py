import os, sys, re
from lxml import etree
reload(sys)
sys.setdefaultencoding('utf8')

dirs = os.path.join(os.getcwd(), "Kar")
ltdir = os.listdir(dirs)



for s in ltdir:
	tree = etree.parse(os.path.join(dirs, s))
	root = tree.getroot()
	# root.set("height", "19.3mm")
	# et = etree.ElementTree(root)
	# et.write(os.path.join(dirs, s))
	print root.get("height")



# for s in ltdir:
# 	f = s.strip(".svg").encode('raw_unicode_escape').strip("\\").split("\\")
# 	if (len(f) == 1):
# 		os.rename(os.path.join(dirs, s), os.path.join(dirs, f[0] + ".svg"))
# 	else:
# 		os.rename(os.path.join(dirs, s), os.path.join(dirs, "_".join(f) + ".svg"))
