#!/usr/bin/python

from sys import exit
from optparse import OptionParser
from os import walk
import os

usage = "usage: %prog [options] src dst"
parser = OptionParser(usage=usage)
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-r", "--reverse",
                  action="store_true", dest="reverse", default=False,
                  help="reverse direction")

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

if options.reverse:
    src, dst = dst, src

entries = walk(src)
dirs_created = set()
files_to_ignore = set(['.DS_Store'])
print 'set -x'
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
        if filename in files_to_ignore:
            continue
        filerelpath = os.path.join(dirpath, filename)
        # print filerelpath
        srcpath = src + filerelpath
        dstpath = dst + filerelpath
        dstdirpath = dst + dirpath
        if not os.path.exists(dstdirpath) and (dstdirpath not in dirs_created):
            print 'mkdir -p "%s"' % dstdirpath
            dirs_created.add(dstdirpath)
        if not os.path.exists(dstpath):
            print 'cp -p "%s" "%s"' % (srcpath, dstpath)
    #print '------'
