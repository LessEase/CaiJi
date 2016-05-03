# sh split.sh ijcai2016_koubei_train 4 20150700 20151100 outputfile
infile=$1
col=$2
begin=$3
end=$4
outfile=$5

awk -F',' '{if($'$col'>'$begin' && $'$col'<'$end')print $0}' $infile > $outfile 
