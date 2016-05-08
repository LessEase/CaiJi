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

def LoadData(filename):
    global user_map, location_map, merchant_map
    X=[]
    Y=[]
    info=[]
    with open(filename,"r") as fin:
        for line in fin:
            frags = line.strip().split("\t")
            if len(frags) != 4:
                continue
            Y.append(int(frags[0]))
            uid = frags[1]
            lid = frags[2]
            mid = frags[3]
            temp = []
            temp += getFeatureUtil.getUserFeature(user_map, uid, lid, mid, True)
            temp += getFeatureUtil.getLocationFeature(location_map, lid, True)
            temp += getFeatureUtil.getMerchantFeature(merchant_map,mid,lid)
            X.append(temp)
            info.append(uid+","+lid+","+mid)
    return X, Y,info
    

if __name__ == "__main__":
    train_file = sys.argv[1]
    user_feature_file = "../../gen_data/user_feature_Before11.pkl"
    location_feature_file = "../../gen_data/location_feature_Before11.pkl"
    merchant_feature_file = "../../gen_data/merchant_feature_Before11"
    user_map = cPickle.load(open(user_feature_file,"r"))
    location_map = cPickle.load(open(location_feature_file,"r"))
    merchant_map = cPickle.load(open(merchant_feature_file,"r"))
    trainX,trainY,a = LoadData(train_file)
    print "train load is done" 
    test_file = sys.argv[2]
    #testX,testY,testInfo = LoadData(test_file)
    print "test load is done"    
    clf = RandomForestClassifier(n_estimators=300, criterion='gini', max_depth=30, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=0.5, max_leaf_nodes=None, bootstrap=True, oob_score=False, n_jobs=8, random_state=None, verbose=1, warm_start=False, class_weight=None)
    #clf = GradientBoostingClassifier(loss='deviance',n_jobs=-1, learning_rate=0.1, n_estimators=3000, subsample=1.0, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_depth=3, init=None, random_state=None, max_features=0.8, verbose=0, max_leaf_nodes=None, warm_start=False, presort='auto')
    clf.fit(trainX, trainY)
    #clf = joblib.load("RFmodel/rf.m")
    joblib.dump(clf,"RFmodel_maxFeature_changed/rf.m")
    #result = clf.predict(testX)
    #print metrics.classification_report(testY,result)
