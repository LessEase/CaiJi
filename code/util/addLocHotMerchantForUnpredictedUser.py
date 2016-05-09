import sys
import re

location_map = dict()

with open("../../gen_data/hotMerchant.txt","r") as fin:
    for line in fin:
        frags = line.strip().split(",")
        lid = frags[0]
        location_map[lid] = frags[1].split(":")[0]

for line in sys.stdin:
    line = line.strip()
    frags = line.split(",")
    uid = frags[0]
    lid = frags[1]
    if location_map.has_key(lid):
        print uid+","+lid+","+location_map[lid]
