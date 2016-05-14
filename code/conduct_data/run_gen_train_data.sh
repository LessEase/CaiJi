function Gen_data()
{
    #生成11月份的训练数据，有正例、负例
    python gen_train_data.py ../validate/data/koubei_splited_train_data_Nov ../validate/data/train_temp 1
    awk -F'\t' '{if($1==1)print $0}' ../validate/data/train_temp > ../validate/data/trainSample_positive
    awk -F'\t' '{if($1==0)print $0}' ../validate/data/train_temp > ../validate/data/trainSample_negative
    #生成11月的验证数据，有正例、负例
    python gen_train_data.py ../validate/data/koubei_splited_val_data_Nov ../validate/data/validationSample 1
    #python gen_train_data.py ../../ori_data/ijcai2016_koubei_test ../../gen_data/testSample 2
}

function Sample()
{
    positive_num=`cat ../validate/data/trainSample_positive | wc -l`
    negative_num=`cat ../validate/data/trainSample_negative | wc -l`
    sample_num=$[ $positive_num * 10 ]
    python randomSampling.py $negative_num $sample_num ../validate/data/trainSample_negative  ../validate/data/trainSample_negative_sampling 
    cat ../validate/data/trainSample_positive ../validate/data/trainSample_negative_sampling  > ../validate/data/trainSample
}

function Run()
{
    Gen_data;
    Sample;
}

Run;
