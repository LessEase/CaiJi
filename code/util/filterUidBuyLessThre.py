import sys
import re

for line in sys.stdin:
    line = line.strip()
    frags = line.split(",")
    uid = frags[0]
    lid = frags[1]
    mids = frags[2]
    if len(mids.split(":"))<3:
        print line
