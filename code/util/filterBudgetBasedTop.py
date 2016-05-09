import sys
import re

map = dict()
merchant_map = dict()
uid_buy = dict()

with open("../../ori_data/ijcai2016_merchant_info","r") as fin:
    for line in fin:
        frags = line.strip().split(",")
        mid = frags[0]
        budget = int(frags[1])
        merchant_map[mid] = budget

with open("../../gen_data/csy_xgboost_result_top2.txt","r") as fin:
    for line in fin:
        frags = line.strip().split(",")
        uid = frags[0]
        lid = frags[1]
        mids = frags[2]
        if not uid_buy.has_key(uid+","+lid):
            uid_buy[uid+","+lid] = set()
        uid_buy[uid+","+lid].add(mids)
        #uid_buy[uid+","+lid] = mids
        if not map.has_key(mids):
            map[mids] = 0
        map[mids] += 1
        '''
        for mid in mids.split(":"):
            if not map.has_key(mid):
                map[mid] = 0
            map[mid] += 1'''

for line in sys.stdin:
    line = line.strip()
    frags = line.split(",")
    uid = frags[0]
    lid = frags[1]
    mid = frags[2]
    if uid_buy.has_key(uid+","+lid) and mid in uid_buy[uid+","+lid]:
        continue
    if not map.has_key(mid):
        map[mid] = 0
    if map[mid] < merchant_map[mid]:
        print uid + "," + lid+","+mid
        map[mid] += 1
for k,v in uid_buy.iteritems():
    for mid in v:
        print k+","+mid
