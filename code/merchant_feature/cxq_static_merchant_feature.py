import sys
import re
import cPickle
import numpy

map = dict()

class MerchantFeature(object):
    def __init__(self):
        self.budget = 0
        self.numOfLoc = 0
        self.total_bought = 0
        self.specific_location_feature = dict()
        self.specific_user_buy = set()

if __name__ == "__main__":
    merchantInfo = "../../ori_data/ijcai2016_merchant_info"
    with open(merchantInfo,"r") as fin:
        for line in fin:
            frags = line.strip().split(",")
            if len(frags)!=3:
                continue
            merchantId = frags[0]
            budget = frags[1]
            numOfLoc = len(frags[2].split(":"))
            merchantObject = MerchantFeature()
            merchantObject.budget = budget
            merchantObject.numOfLoc = numOfLoc
            map[merchantId] = merchantObject
    koubeiTrain = "../../gen_data/ijcai2016_koubei_trainAfter7"
    with open(koubeiTrain,"r") as fin:
        for line in fin:
            frags = line.strip().split(",")
            if len(frags) != 4:
                continue
            userId = frags[0]
            merchantId = frags[1]
            locationId = frags[2]
            time = frags[3]
            map[merchantId].total_bought += 1
            map[merchantId].specific_user_buy.add(userId)
            if not map[merchantId].specific_location_feature.has_key(locationId):
                map[merchantId].specific_location_feature[locationId]=dict()
                map[merchantId].specific_location_feature[locationId]["bought"] = 0
                map[merchantId].specific_location_feature[locationId]["user"] = set()
                map[merchantId].specific_location_feature[locationId]["date"] = set()
            map[merchantId].specific_location_feature[locationId]["bought"] += 1
            map[merchantId].specific_location_feature[locationId]["user"].add(userId)
            map[merchantId].specific_location_feature[locationId]["date"].add(time)
    result = dict()
    for merchanId, merchantObject in map.iteritems():
        result[merchanId] = dict()
        result[merchanId]["total_bought"] = merchantObject.total_bought
        result[merchanId]["budget"] = merchantObject.budget
        result[merchanId]["numOfLoc"] = merchantObject.numOfLoc
        result[merchanId]["numOfUser"] = len(merchantObject.specific_user_buy)
        result[merchanId]["avg_Loc_buy"] = float(result[merchanId]["total_bought"])/(result[merchanId]["numOfLoc"]+0.1)
        result[merchanId]["avg_User_buy"] = float(result[merchanId]["total_bought"])/(result[merchanId]["numOfUser"]+0.1)
        result[merchanId]["each_location"] = dict()
        each_loc_bought = []
        for locationId, values in merchantObject.specific_location_feature.iteritems():
            users = len(values["user"])
            days = len(values["date"])
            boughts = values["bought"]
            each_loc_bought.append(boughts)
            result[merchanId]["each_location"][locationId] = dict()
            result[merchanId]["each_location"][locationId]["boughts"] = boughts
            result[merchanId]["each_location"][locationId]["users"] = users
            result[merchanId]["each_location"][locationId]["days"] = days
            result[merchanId]["each_location"][locationId]["percent_loc_bought"] = float(boughts)/(merchantObject.total_bought+0.1)
            result[merchanId]["each_location"][locationId]["per_day_loc_bought"] = float(boughts)/(days+0.1)
            result[merchanId]["each_location"][locationId]["percent_loc_user"] = float(users)/(result[merchanId]["numOfUser"]+0.1)
            result[merchanId]["each_location"][locationId]["per_day_loc_user"] = float(users)/(days+0.1)
        if len(each_loc_bought) > 0 :
            result[merchanId]["sigma_location"] = numpy.var(each_loc_bought)
        else:
            result[merchanId]["sigma_location"] = 0.0
    merchantFatureFile = "../../gen_data/cxq_koubei_merchant_feature_After7"
    myfile = file(merchantFatureFile,"w")
    cPickle.dump(result,myfile)

