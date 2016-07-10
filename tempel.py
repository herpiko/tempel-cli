#!/usr/bin/python

import urllib, urllib2
import sys, getopt

def bantuan():
    string = """
    Usage: tempel.py [options]
    Options:

        -h, --help             output usage information
        -V, --version          output the version number
        -l, --language <lang>  Set language
        -t, --text <text>      From text
    
    tempel.py -l <lang> -t <text>"""
    print string

def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:l:t:",["language=","text="])
    except getopt.GetoptError:
        bantuan()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            bantuan()
            sys.exit()
        elif opt in ("-l", "--language"):
            lang = arg
        elif opt in ("-t", "--text"):
            text = arg
        else:
            assert False, "unhandled option"
    tempel = 'http://tempel.blankon.in'
    values = {
      'language' : lang,
      'content' : text
    }
    data = urllib.urlencode(values)
    print data
    response = urllib2.urlopen(urllib2.Request(tempel,data)) 
    print 'URL     :', response.geturl()

if __name__ == "__main__":
   main(sys.argv[1:])