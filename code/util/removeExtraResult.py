import sys
import re

map = dict()
merchant_map = dict()

with open("../../ori_data/ijcai2016_merchant_info","r") as fin:
    for line in fin:
        frags = line.strip().split(",")
        mid = frags[0]
        budget = frags[1]
        merchant_map[mid] = budget
pre_mid = ""
for line in sys.stdin:
    frags = line.strip().split(",")
    uid = frags[0]
    lid = frags[1]
    mid = frags[2]
    score = float(frags[3])
    i = 0
    if mid != pre_mid:
        pre_mid = mid
        i = 1
        if i <= merchant_map[pre_mid]:
            print uid + "," + lid + "," + mid
    else:
        i+=1
        if i <= merchant_map[pre_mid]:
            print uid + "," + lid + "," + mid



