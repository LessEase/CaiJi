import sys
import re
import cPickle
import math
sys.path.append('../util')
import getFeatureUtil
import numpy
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import metrics
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegressionCV
from sklearn.cross_validation import cross_val_score

user_map = dict()
location_map = dict()
merchant_map = dict()

user_feature_file = ""
location_feature_file = ""
merchant_feature_file = ""


if __name__ == "__main__":
    user_feature_file = "../../gen_data/user_feature_After7.pkl"
    location_feature_file = "../../gen_data/location_feature_After7.pkl"
    merchant_feature_file = "../../gen_data/merchant_feature_After7"
    user_map = cPickle.load(open(user_feature_file,"r"))
    location_map = cPickle.load(open(location_feature_file,"r"))
    merchant_map = cPickle.load(open(merchant_feature_file,"r"))
    clf = RandomForestClassifier(n_estimators=300, criterion='gini', max_depth=20, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=0.8, max_leaf_nodes=None, bootstrap=True, oob_score=False, n_jobs=4, random_state=None, verbose=0, warm_start=False, class_weight=None)
    clf = joblib.load("RFmodel/rf.m")
    out = file("../../gen_data/result2.txt","w")
    testX = []
    testY = []
    testInfo = []
    for line in sys.stdin:
        frags = line.strip().split("\t")
        if len(frags) != 4:
            continue
        testY.append(int(frags[0]))
        uid = frags[1]
        lid = frags[2]
        mid = frags[3]
        temp = []
        temp += getFeatureUtil.getUserFeature(user_map, uid, lid, mid, True)
        temp += getFeatureUtil.getLocationFeature(location_map, lid, True)
        temp += getFeatureUtil.getMerchantFeature(merchant_map,mid,lid)
        testX.append(temp)
        testInfo.append(uid+","+lid+","+mid)
        if len(testY) > 100000:
            result = clf.predict(testX)
            for i in range(len(result)):
                if result[i] == 1:
                    out.write(testInfo[i]+"\n")
            testX = []
            testY = []
            testInfo = []
    result = clf.predict(testX)
    for i in range(len(result)):
        if result[i] == 1:
            out.write(testInfo[i]+"\n")

    #print metrics.classification_report(testY,result)
