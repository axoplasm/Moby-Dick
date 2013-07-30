# coding=utf-8 
#!/usr/bin/python

import re
import codecs # this totally fixes my unicode problems. See: http://www.evanjones.ca/python-utf8.html
import os

infile = codecs.open("chapter/049-hyena.md", "r", "utf-8")
#outfile = codecs.open("outfile.md", "w", "utf-8")

for line in infile:
	line = re.sub('^"','“',line.rstrip())
	print(line)
