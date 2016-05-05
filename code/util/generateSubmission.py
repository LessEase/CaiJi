
import sys

if __name__ == "__main__":

    infile = sys.argv[1]
    outfile = sys.argv[2]


    result = dict()
    with open(infile, "r") as fin:
        for line in fin:
            items = line.strip().split(",")
            uid = items[0]
            lid = items[1]
            mid = items[2]
            if uid not in result:
                result[uid] = dict()

            if lid not in result[uid]:
                result[uid][lid] = set()

            result[uid][lid].add(mid)

    with open(outfile, "w") as fout:
        for uid in result:
            line = ""
            for lid, mids in result[uid].items():
                line = uid + "," + lid + "," + ":".join(list(mids))
            fout.write(line + "\n")


            

    
