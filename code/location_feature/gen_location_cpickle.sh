#########################################################################
# File Name: gen_location_cpickle.sh
# Author: csy
# mail: chshaoyi7@gmail.com
# Created Time: Wed 04 May 2016 07:30:54 PM CST
#########################################################################
#!/bin/bash


python csy_count_location_feature.py ../../gen_data/ijcai2016_koubei_train_Before11 ../../gen_data/location_feature_Before11.pkl
python csy_count_location_feature.py ../../gen_data/ijcai2016_koubei_train_After7 ../../gen_data/location_feature_After7.pkl

