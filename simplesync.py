#!/usr/bin/python

from sys import exit
from optparse import OptionParser
from os import walk
import os

usage = "usage: %prog [options] src dst"
parser = OptionParser(usage=usage)
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

if len(args) < 2:
    parser.print_usage()
    exit(1)

src = args[0]
dst = args[1]

if src.endswith(os.sep):
    src = src[:-1]

if dst.endswith(os.sep):
    dst = dst[:-1]

entries = walk(src)

for dirpath, dirnames, filenames in entries:
    dirpath = dirpath[len(src):]
    if len(dirpath) == 0:
        dirpath = os.sep
    #print 'dirpath: %s' % dirpath

    #print 'dirnames:'
    #for dirname in dirnames:
    #    print '- %s' % dirname

    #print 'filenames:'
    for filename in filenames:
        filerelpath = os.path.join(dirpath, filename)
        # print filerelpath
        srcpath = src + filerelpath
        dstpath = dst + filerelpath
        if not os.path.exists(dstpath):
            print 'cp -p "%s" "%s"' % (srcpath, dstpath)
    #print '------'
