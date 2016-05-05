function Gen_data()
{
    python gen_train_data.py ../../gen_data/ijcai2016_koubei_trainNov ../../gen_data/train_temp 1
    awk -F'\t' '{if($1==1)print $0}' ../../gen_data/train_temp > ../../gen_data/trainSample_positive
    awk -F'\t' '{if($1==0)print $0}' ../../gen_data/train_temp > ../../gen_data/trainSample_negative
    python gen_train_data.py ../../ori_data/ijcai2016_koubei_test ../../gen_data/testSample 2
}

function Sample()
{
    positive_num=`cat ../../gen_data/trainSample_positive | wc -l`
    negative_num=`cat ../../gen_data/trainSample_negative | wc -l`
    sample_num=$[ $positive_num * 2 ]
    python randomSampling.py $negative_num $sample_num ../../gen_data/trainSample_negative ../../gen_data/trainSample_negative_sampling
    cat ../../gen_data/trainSample_positive ../../gen_data/trainSample_negative_sampling > ../../gen_data/trainSample
}

function Run()
{
    Gen_data;
    Sample;
}

Run;
