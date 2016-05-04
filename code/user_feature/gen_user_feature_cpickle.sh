#########################################################################
# File Name: gen_user_feature_cpickle.sh
# Author: csy
# mail: chshaoyi7@gmail.com
# Created Time: Wed 04 May 2016 09:09:35 PM CST
#########################################################################
#!/bin/bash


python csy_count_user_feature.py ../../gen_data/ijcai2016_koubei_trainAfter7 ../../gen_data/user_feature_After7.pkl 
python csy_count_user_feature.py ../../gen_data/ijcai2016_koubei_trainBefore11 ../../gen_data/user_feature_Before11.pkl 

