python gen_train_data.py ../../gen_data/ijcai2016_koubei_trainNov ../../gen_data/trainSample 1
awk -F'\t' '{if($1==1)print $0}' ../../gen_data/trainSample > ../../gen_data/trainSample_positive
awk -F'\t' '{if($1==0)print $0}' ../../gen_data/trainSample > ../../gen_data/trainSample_negative
python gen_train_data.py ../../ori_data/ijcai2016_koubei_test ../../gen_data/testSample 2
