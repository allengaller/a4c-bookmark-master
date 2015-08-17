# Allen Galler
# allengaller@gmail.com
# http://yalun.org

import urllib2
from HTMLParser import HTMLParser

class bm_loader():
    orig_bm = open('bookmarks_7_4_12.html','r')
    try:
        orig_bm_str = orig_bm.read()
        print orig_bm_str.split()
    finally:
        orig_bm.close()

def Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        print 0

    def handle_starttag(self, tag, attrs):
        print AAA
        for (variable, value) in attrs:
            print variable
            print 1
        if tag == "A":
            if len(attrs) == 0: print 1
            else:
                print 2
                for(variable, value) in attrs:
                    if variable == "HREF" : self.links.append(value)
        print self.links
        return self.links
    

if __name__ == "__main__":
    bm_orig = bm_loader()
    #print bm_orig.orig_bm_str
    raw_str = bm_orig.orig_bm_str
    #print raw_str
    href_list = Parser(raw_str)
    
    #print href_list
    print "END OF FILE"
