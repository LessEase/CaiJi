#########################################################################
# File Name: gen_predicted_positive_sample.sh
# Author: csy
# mail: chshaoyi7@gmail.com
# Created Time: Sat 07 May 2016 03:50:10 PM CST
#########################################################################
#!/bin/bash

python trans_score_to_result.py ../../../gen_data/testSample pred.txt ../../../gen_data/xgboost_predicted_result

