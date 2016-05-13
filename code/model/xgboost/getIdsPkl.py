
import cPickle

def gen_ids_map():
	infile = "../../../ori_data/ijcai2016_merchant_info"
	merchantIdMap = dict()
	locationIdMap = dict()
	merchantId = 1
	locationId = 1
	with open(infile, "r") as fin:
		for line in fin: 
			frags = line.strip().split(",")
			mid = frags[0]
			ids = frags[2].split(":")
			if mid not in merchantIdMap:
				merchantIdMap[mid] = merchantId
				merchantId += 1
			for id in ids:
				if id not in locationIdMap:
					locationIdMap[id] = locationId
					locationId += 1
	
	cPickle.dump(locationIdMap, open("location_id_map.pkl","w"))
	cPickle.dump(merchantIdMap, open("merchant_id_map.pkl", "w"))

gen_ids_map()

