import sys
import re
import cPickle

loc2mid = dict()
user_buy = dict()

def gen_train(data_file,out_file):
    global loc2mid, user_buy
    with open(data_file,"r") as fin:
        for line in fin:
            frags = line.strip().split(",")
            user = frags[0]
            mid = frags[1]
            locId = frags[2]
            if not user_buy.has_key(user):
                user_buy[user] = dict()
            if not user_buy[user].has_key(locId):
                user_buy[user][locId] = dict()
            if not user_buy[user][locId].has_key(mid):
                user_buy[user][locId][mid] = 0
            user_buy[user][locId][mid] += 1
    out = file(out_file,"w")
    #print negative data , 2: user did not buy in this location
    for user, buyMap in user_buy.iteritems():
        for loc,midMap in buyMap.iteritems():
            mids = loc2mid[loc]
            for mid in mids:
                if not midMap.has_key(mid):
                    out.write("0\t"+user+"\t"+loc+"\t"+mid+"\n")
                else:
                    for i in range(midMap[mid]):
                        out.write("1\t"+user+"\t"+loc+"\t"+mid+"\n")

    '''    
        for loc, mids in loc2mid.iteritems():
            #user bought in this loc
            if buyMap.has_key(loc):
                for mid in mids:
                    if not buyMap[loc].has_key(mid):
                        out.write("0\t"+user+"\t"+loc+"\t"+mid+"\n")
    #print positive data
    for user, buyMap in user_buy.iteritems():
        for loc, midMap in buyMap.iteritems():
            for mid, num in midMap.iteritems():
                print str(num)
                for i in range(num):
                    out.write("1\t"+user+"\t"+loc+"\t"+mid+"\n")'''

def gen_test(data_file,out_file):
    global user_buy, loc2mid
    out = file(out_file,"w")
    with open(data_file,"r") as fin:
        for line in fin:
            frags = line.strip().split(",")
            user = frags[0]
            locId = frags[1]
            for mid in loc2mid[locId]:
                out.write("0\t"+user+"\t"+locId+"\t"+mid+"\n")

if __name__=="__main__":
    with open("../../ori_data/ijcai2016_merchant_info","r") as fin:
        for line in fin:
            frags = line.strip().split(",")
            locList = frags[2].split(":")
            mid = frags[0]
            for loc in locList:
                if not loc2mid.has_key(loc):
                    loc2mid[loc] = set()
                loc2mid[loc].add(mid)

    #data_file = "../../gen_data/ijcai2016_koubei_trainNov"
    data_file = str(sys.argv[1])
    out_file = str(sys.argv[2])
    flag = int(sys.argv[3])
    if flag==1:
        gen_train(data_file,out_file)
    else:
        gen_test(data_file,out_file)
