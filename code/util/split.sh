# sh split.sh ijcai2016_koubei_train 4 20150700 20151100 outputfile

awk -F',' '{if($4<"20151100")print $0}' ../validate/koubei_splited_train_data > ../validate/data/koubei_splited_train_data_Before11
awk -F',' '{if($4>"20151100")print $0}' ../validate/koubei_splited_train_data > ../validate/data/koubei_splited_train_data_Nov
awk -F',' '{if($4<"20151100")print $0}' ../validate/koubei_splited_val_data > ../validate/data/koubei_splited_val_data_Before11
