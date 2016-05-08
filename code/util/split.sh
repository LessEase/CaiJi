# sh split.sh ijcai2016_koubei_train 4 20150700 20151100 outputfile

awk -F',' '{if($4>"20151123" && $4<"20151200")print $0}' ../../gen_data/ijcai2016_koubei_trainNov > ../../gen_data/ijcai2016_koubei_trainNov_24_30
awk -F',' '{if($4>"20151100" && $4<"20151124")print $0}' ../../gen_data/ijcai2016_koubei_trainNov > ../../gen_data/ijcai2016_koubei_trainNov_01_23
