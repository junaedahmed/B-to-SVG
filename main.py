from __future__ import print_function
from lxml import etree
import re

import os, sys
import svg_stack as ss

reload(sys)
sys.setdefaultencoding('utf8')

dirs = os.path.join(os.getcwd(), "character")
ltdir = os.listdir(dirs)

txt = open(sys.argv[1], "r")
dt = txt.readlines()
txt.close()
fd = open(sys.argv[1].split(".")[0] + ".svg", mode ="w")

doc = ss.Document()

layout = ss.HBoxLayout()


for line in dt:
	data = unicode(line.strip("\n")).split(" ")

	for word in data:
		ud = word.encode('raw_unicode_escape').strip("\\").split("\\")
		ind = [i for i, x in enumerate(ud) if x == 'u09c7' or x == 'u09bf']

		for i in ind:
			ud[i-1], ud[i] = ud[i], ud[i-1]
		print(ud)
		it = 0
		while(len(ud) >= it):
			glyf5 = '_'.join(ud[it:it+5]).strip("_").replace(" ", "") + ".svg"
			glyf4 = '_'.join(ud[it:it+4]).strip("_").replace(" ", "") + ".svg"
			glyf3 = '_'.join(ud[it:it+3]).strip("_").replace(" ", "") + ".svg"
			glyf2 = '_'.join(ud[it:it+2]).strip("_").replace(" ", "") + ".svg"
			glyf1 = '_'.join(ud[it:it+1]).strip("_").replace(" ", "") + ".svg"
			glyft = '_'.join(ud[it-1:it]).strip("_").replace(" ", "") + ".svg"

			if (glyf5 in ltdir):
				it += 5
				layout.addSVG(os.path.join(dirs, glyf5))
			elif(glyf4 in ltdir):
				it += 4
				layout.addSVG(os.path.join(dirs, glyf4))
			elif(glyf3 in ltdir):
				it += 3
				layout.addSVG(os.path.join(dirs, glyf3))
			elif(glyf2 in ltdir):
				it += 2
				layout.addSVG(os.path.join(dirs, glyf2))
			else:
				if (glyf1 == 'u09c0.svg'):
					dc = ss.Document()
					lt = ss.HBoxLayout()
					tmp = open('tmp.svg',mode='w')
					lt.addSVG(os.path.join(dirs, glyft))
					lt.addSVG(os.path.join(dirs, glyf1))
					lt.setSpacing(-30)
					dc.setLayout(lt)
					dc.save(tmp)
					print(tmp)
					tmp.close()
					layout.addSVG(os.path.join(os.getcwd(), "tmp.svg"))
					it += 1
				else:
					layout.addSVG(os.path.join(dirs, glyf1))
					it += 1
		layout.addSVG(os.path.join(dirs, "space.svg"))

doc.setLayout(layout)
doc.save(fd)