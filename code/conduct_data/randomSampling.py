import sys
import re
from numpy import random

if __name__=="__main__":
    total_num = int(sys.argv[1])
    num = int(sys.argv[2])
    index_set = set(random.choice(total_num,num,False))
    map = dict()
    infile = sys.argv[3]
    outfile = sys.argv[4]
    out = open(outfile,"w")
    i=0
    with open(infile,"r") as fin:
        for line in fin:
            line = line.strip()
            if line =="":
                continue
            map[i] = line
            i+=1
    for index in index_set:
        out.write(map[index]+"\n")
