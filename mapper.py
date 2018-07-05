#!/usr/bin/env python

from xml.dom.minidom import parse
import xml.dom.minidom
import sys

#file = "/root/Desktop/xml-test/wiki.xml"

file = sys.stdin

DOMTree = xml.dom.minidom.parse(file)
mediawiki = DOMTree.documentElement

titles = mediawiki.getElementsByTagName('title')
texts = mediawiki.getElementsByTagName('text')
#print("Title: %s" % title.childNodes[0].data)
#print("Content: %s" % text.childNodes[0].data)
no_of_pages = len(mediawiki.getElementsByTagName('title'))

for i in range(0,no_of_pages):
	
	title =  titles[i].childNodes[0].data
	text = texts[i].childNodes[0].data
	
	if(text == ""):
		continue

	links = []
	while(text.find("[[") != -1):
		start = text.index("[[")
		end = text.index("]]")

		l = list(text)
		links.append(text[start+2:end])
	
		l[start] = '|'
		l[end]  = '|'

		text = "".join(l)

	no_of_links = len(links)
	credits = float(1/no_of_links)
	for i in range(0 , no_of_links):
		print('%s\t%s' % (links[i],credits))


