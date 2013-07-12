#!usr/bin/env python

import urllib2
import sys

def share(nasdaqsym):

 share_link = 'http://download.finance.yahoo.com/d/quotes.csv?s='+nasdaqsym+'&f=l1'

 s_value = urllib2.urlopen(share_link)

 s = s_value.read()

 print 'Latest share value of '+nasdaqsym+'is: '+s

if __name__=='__main__':
    if len(sys.argv) == 2:
        share(sys.argv[1])
    else:
        print "Error! Two NASDAQ symbols cannot be given at a time"
    sys.exit(0)

