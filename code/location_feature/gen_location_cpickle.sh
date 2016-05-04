#########################################################################
# File Name: gen_location_cpickle.sh
# Author: csy
# mail: chshaoyi7@gmail.com
# Created Time: Wed 04 May 2016 07:30:54 PM CST
#########################################################################
#!/bin/bash


#python csy_count_location_feature.py  infile  outfile
python csy_count_location_feature.py ../../gen_data/ijcai2016_koubei_trainBefore11 ../../gen_data/location_feature_Before11.pkl
python csy_count_location_feature.py ../../gen_data/ijcai2016_koubei_trainAfter7 ../../gen_data/location_feature_After7.pkl

