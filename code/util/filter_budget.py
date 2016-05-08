import sys
import re

map = dict()
merchant_map = dict()

with open("../../ori_data/ijcai2016_merchant_info","r") as fin:
    for line in fin:
        frags = line.strip().split(",")
        mid = frags[0]
        budget = int(frags[1])
        merchant_map[mid] = budget
pre_mid = ""
i = 0
for line in sys.stdin:
    frags = line.strip().split(",")
    uid = frags[0]
    lid = frags[1]
    mid = frags[2]
    score = float(frags[3])
    if mid != pre_mid:
        pre_mid = mid
        pre_user = uid
        pre_lic = lid
        if i> merchant_map[mid]:
            print mid + "\t" + str(i)
        i = 1
        #if i <= merchant_map[mid]:
           # print uid + "," + lid + "," + mid
    else:
        i+=1
        #if i <= merchant_map[mid]:
        #    print uid + "," + lid + "," + mid
        #if i> merchant_map[mid]:
         #   print mid + "\t" + str(i)


