# sh split.sh ijcai2016_koubei_train 4 20150700 20151100 outputfile
infile="../../ori_data/ijcai2016_koubei_train"
col=4
begin=$1
end=$2
outfile=$3

awk -F',' '{if($'$col'>'$begin' && $'$col'<'$end')print $0}' $infile > $outfile 
