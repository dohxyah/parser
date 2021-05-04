#!/usr/bin/python

import re
import argparse
import os.path
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-r", "--regex", nargs='+', help="Regex pattern", required=True)
parser.add_argument("-f", "--file", help="File to parse")

args = parser.parse_args()
patterns = args.regex
line_num = 0

filename = "file.txt"

if os.path.isfile(filename):
   print('Looking for {} in {} '.format(patterns, filename))
else:
   print('Please enter you text, for the exit please type "quit"')
   f = open("file.txt", "w")
   while True:
       line = sys.stdin.readline().rstrip('\n')
       if line == 'quit':
           break
       else:
           f.write(line + '\n')
           for pattern in patterns:
              if re.search(pattern, line):
                  print('Found a match for {} in {}'.format(pattern, line))

filehandle = open(filename, 'r')

while True:
    line = filehandle.readline()
    line_num += 1
    if not line:
        break

    for pattern in patterns:
        if re.search(pattern, line):
            print('Found a match for {} in {} line {}'.format(pattern, line_num, line))

filehandle.close()
