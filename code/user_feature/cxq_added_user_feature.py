import sys
import re
import cPickle
import datetime

class UserObject(object):
    
    def __init__(self):
        self.month_active = dict()
        self.active_num = set()
        self.earliest_active = ""
        self.latest_active = ""
        self.month_bought = dict()
        self.lid_map = dict()
        self.mid_map = dict()

userMap = dict()
result = dict()
default1 = 200
default2 = 300
out_file = sys.argv[1]
flag = int(sys.argv[2])
currentTime = "20151101" # train
if flag != 1:
    currentTime = "20151201"

for line in sys.stdin:
    frags = line.strip().split(",")
    uid = frags[0]
    mid = frags[1]
    lid = frags[2]
    time = frags[3]
    month = time[4:6]
    if not userMap.has_key(uid):
        userMap[uid] = UserObject()
    if userMap[uid].earliest_active == "":
        userMap[uid].earliest_active = time
        userMap[uid].latest_active = time
    else:
        if userMap[uid].earliest_active > time:
            userMap[uid].earliest_active = time
        if userMap[uid].latest_active < time:
            userMap[uid].latest_active = time
    
    if not userMap[uid].month_active.has_key(month):
        userMap[uid].month_active[month] = set()
    userMap[uid].month_active[month].add(time)
    userMap[uid].active_num.add(time)
    
    if not userMap[uid].month_bought.has_key(month):
        userMap[uid].month_bought[month] = []
    userMap[uid].month_bought[month].append(time)
    
    if not userMap[uid].lid_map.has_key(lid):
        userMap[uid].lid_map[lid] = dict()
    if not userMap[uid].lid_map[lid].has_key(mid):
        userMap[uid].lid_map[lid][mid] = []
    userMap[uid].lid_map[lid][mid].append(time)
    
    if not userMap[uid].mid_map.has_key(mid):
        userMap[uid].mid_map[mid] = dict()
        userMap[uid].mid_map[mid]["bought"] = []
        userMap[uid].mid_map[mid]["boughtNum"] = 0
        userMap[uid].mid_map[mid]["month"] = dict()
    userMap[uid].mid_map[mid]["bought"].append(time)
    userMap[uid].mid_map[mid]["boughtNum"] += 1
    if not userMap[uid].mid_map[mid]["month"].has_key(month):
        userMap[uid].mid_map[mid]["month"][month] = []
    userMap[uid].mid_map[mid]["month"][month].append(time)

for uid, userObject in userMap.iteritems():
    result[uid] = dict()
    earliestTime = userObject.earliest_active
    result[uid]["earliest"] = (datetime.datetime(int(currentTime[0:4]),int(currentTime[4:6]),int(currentTime[6:8]))\
            - datetime.datetime(int(earliestTime[0:4]),int(earliestTime[4:6]),int(earliestTime[6:8]))).days
    latestTime = userObject.latest_active
    result[uid]["latest"] = (datetime.datetime(int(currentTime[0:4]),int(currentTime[4:6]),int(currentTime[6:8]))\
            - datetime.datetime(int(latestTime[0:4]),int(latestTime[4:6]),int(latestTime[6:8]))).days
    result[uid]["month_active"] = dict()
    for month, value in userObject.month_active.iteritems():
        result[uid]["month_active"][month] = len(value)
    result[uid]["active_total"] = len(userObject.active_num)
    result[uid]["month_bought"] = dict()
    result[uid]["month_period_bought"] = dict()
    for month, timeList in userObject.month_bought.iteritems():
        result[uid]["month_bought"][month] = len(timeList)
        if len(timeList) == 1:
            result[uid]["month_period_bought"][month] = default1
        else:
            maxTime = max(timeList)
            minTime = min(timeList)
            period = (datetime.datetime(int(maxTime[0:4]),int(maxTime[4:6]),int(maxTime[6:8]))\
                    - datetime.datetime(int(minTime[0:4]),int(minTime[4:6]),int(minTime[6:8]))).days+1
            result[uid]["month_period_bought"][month] = float(period)/len(timeList)
    
    result[uid]["location"]  = dict()
    for lid, merchants in userObject.lid_map.iteritems():
        result[uid]["location"][lid] = dict()
        result[uid]["location"][lid]["merchant"] = dict()
        lid_bought = 0
        for mid, timeList in merchants.iteritems():
            result[uid]["location"][lid]["merchant"][mid]= dict()
            result[uid]["location"][lid]["merchant"][mid]["bought"] = len(timeList)
            lid_bought += len(timeList)
            minTime = min(timeList)
            maxTime = max(timeList)
            result[uid]["location"][lid]["merchant"][mid]["earliest"] =(datetime.datetime(int(currentTime[0:4]),int(currentTime[4:6]),int(currentTime[6:8]))\
                    -datetime.datetime(int(minTime[0:4]),int(minTime[4:6]),int(minTime[6:8]))).days
            result[uid]["location"][lid]["merchant"][mid]["latest"] =(datetime.datetime(int(currentTime[0:4]),int(currentTime[4:6]),int(currentTime[6:8]))\
                    -datetime.datetime(int(maxTime[0:4]),int(maxTime[4:6]),int(maxTime[6:8]))).days
        for mid in result[uid]["location"][lid]["merchant"]:
            result[uid]["location"][lid]["merchant"][mid]["bought_percent"] = float(result[uid]["location"][lid]["merchant"][mid]["bought"])/lid_bought
    
    result[uid]["merchant"] = dict()
    mid_rank = dict()
    for mid, mid_buy in userObject.mid_map.iteritems():
        mid_rank[mid] = mid_buy["boughtNum"]
        result[uid]["merchant"][mid] = dict()
        minTime = min(mid_buy["bought"])
        maxTime = max(mid_buy["bought"])
        result[uid]["merchant"][mid]["earliest"] =(datetime.datetime(int(currentTime[0:4]),int(currentTime[4:6]),int(currentTime[6:8]))\
                -datetime.datetime(int(minTime[0:4]),int(minTime[4:6]),int(minTime[6:8]))).days
        result[uid]["merchant"][mid]["latest"] =(datetime.datetime(int(currentTime[0:4]),int(currentTime[4:6]),int(currentTime[6:8]))\
                -datetime.datetime(int(maxTime[0:4]),int(maxTime[4:6]),int(maxTime[6:8]))).days
        result[uid]["merchant"][mid]["month_period_bought"] = dict()
        for month, timeList in mid_buy["month"].iteritems():
            if len(timeList) == 1:
                result[uid]["merchant"][mid]["month_period_bought"][month] = default1
            else:
                maxTime = max(timeList)
                minTime = min(timeList)
                period = (datetime.datetime(int(maxTime[0:4]),int(maxTime[4:6]),int(maxTime[6:8]))\
                        -datetime.datetime(int(minTime[0:4]),int(minTime[4:6]),int(minTime[6:8]))).days+1
                result[uid]["merchant"][mid]["month_period_bought"][month] = float(period)/len(timeList)
    temp = sorted(mid_rank.items(), key=lambda d:d[1], reverse=True)
    result[uid]["merchant_rank"] = dict()
    for i in range(len(temp)):
        result[uid]["merchant_rank"][temp[i][0]] = i+1
out = open(out_file,"w")
cPickle.dump(result, out)
out.close()
     
