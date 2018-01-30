import os, sys
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf8')

glyphname = []

with open("kalpurush.svg", "r") as f:
	doc = etree.parse(f)
	root = doc.getroot()
	for g in root.getchildren()[1].getchildren()[0].getchildren():
		if "glyph-name" in g.attrib:
			glyphname.append(g.attrib['glyph-name'])

with open("glyph-name.txt", "a+") as g:
	for n in glyphname:
		g.write(n+"\n")

	print g.read()