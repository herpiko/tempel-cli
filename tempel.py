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
    content = ""
    lang = "plain"

    if len(argv) < 1:
        bantuan()
        sys.exit(2)
    elif len(argv) == 1:
        if argv[0] == "-h" or argv[0] == "--help":
            bantuan()
            sys.exit(2)
        elif argv[0] == "-t" or argv[0] == "--text" or argv[0] == "-l" or argv[0] == "--language":
            bantuan()
            sys.exit(2)
        else:
            f = open(argv[0], "r")
            content = f.readline()
    index = 0
    for arg in argv:
        index = index + 1
        if index%2 == 1:
            if arg == '-l' or arg == '--language':
                lang = argv[index]
            elif arg == '-t' or arg == '--text':
                content = argv[index]
            else:
                if index == len(argv):
                    f = open(arg, "r")
                    content = f.readline()
                else:
                    bantuan()
                    sys.exit(2)

    if content == "":
        bantuan()
        sys.exit(2)

    tempel = 'http://tempel.blankon.in'
    values = {
      'language' : lang,
      'content' : content
    }
    print values
    data = urllib.urlencode(values)

    response = urllib2.urlopen(urllib2.Request(tempel,data))
    print 'URL     :', response.geturl()

if __name__ == "__main__":
   main(sys.argv[1:])
