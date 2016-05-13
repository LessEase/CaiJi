#########################################################################
# File Name: run_transform.sh
# Author: csy
# mail: chshaoyi7@gmail.com
# Created Time: Sat 07 May 2016 10:50:45 AM CST
#########################################################################
#!/bin/bash

#python transform2xgboost_input_format.py  inputfile outputfile isTrain(1/0)
#python transform2xgboost_input_format.py  ../../../gen_data/splited_trainSample ../../../gen_data/splited_xgboost_train_data 1
#python transform2xgboost_input_format.py  ../../../gen_data/splited_val_temp ../../../gen_data/xgboost_val_data 1
python getIdsPkl.py
python transform2xgboost_input_format.py  ../../../gen_data/trainSample ../../../gen_data/xgboost_train_data_1_to_2 1
python transform2xgboost_input_format.py  ../../../gen_data/testSample ../../../gen_data/xgboost_test_data 0

