#!python
from urlparse import urlparse, parse_qs
from os import listdir
from os.path import exists, isdir, basename, join
import sys
import re
from xml.etree.ElementTree import ElementTree
from bs4 import BeautifulSoup
WWWAPP_URL = "http://wwwapp.cc.columbia.edu/ldpd/app/nny/search"
FULLTEXT_URL = "https://fulltext.cul.columbia.edu/nny"

class Whitespace(BeautifulSoup):
  def pushTag(self, tag):
    #print "Push", tag.name
    if self.currentTag:
        self.currentTag.contents.append(tag)
    self.tagStack.append(tag)
    self.currentTag = self.tagStack[-1]
    self.preserve_whitespace_tag_stack.append(tag)

class Transformer:
  def __init__(self):
    pass
  def transform_action(self, input):
    if input == WWWAPP_URL:
      return FULLTEXT_URL
    else:
      return False
  def transform_file(self,input,output):
    if isdir(input): return
    if re.search(r'\.html?$',input) == None: return
    if isdir(output):
      output = join(output,basename(input))
    with open(input,'r') as inputfile:
      src = inputfile.read()
    soup = Whitespace(src, 'html.parser')
    soup.convertHTMLEntities = False
    delta = False
    for f in soup.find_all('form',attrs={'name':'search'}):

      repl = self.transform_action(f.get('action')) if f.get('action') else False
      if repl:
        delta = True
        f['action'] = repl
      for i in f.find_all('input'):
        if i['type'] == 'submit':
          if i.get('onclick'):
            del i['onclick']
            delta = True
        else:
          if i['name'] == 'p':
            i['name'] = 'page'
            delta = True
          if i['name'] == 'hpp':
            i['name'] = 'per_page'
            delta = True
          if i['name'] == 'query':
            i['name'] = 'q'
            delta = True
    if delta:
      src = soup.encode("utf8",formatter="html")
    if (input != output) or delta:
      with open(output,'w') as f: f.write(src)
  def transform(self, input, output):
    if isdir(input):
      for file in listdir(input):
        if not isdir(file):
          try:
            self.transform_file(join(input,file),output)
          except:
            e = sys.exc_info()[0]
            print join(input,file)
            print e
    else:
      self.transform_file(input,output)
