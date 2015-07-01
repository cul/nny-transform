#!python
from optparse import OptionParser
import sys
import wwwapp
if __name__ == '__main__':
  i = sys.argv[1]
  o = sys.argv[2]
  wwwapp.Transformer().transform(i,o)