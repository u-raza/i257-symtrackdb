with open('data/symptoms_dummydata_only.csv') as fin:
	lines = fin.readlines()
	for line in lines:
		lst = line.split(',')
		if len(lst) == 2:
			sym_id, name = lst
		else:
			sym_id, name, _ = lst
		print(line)

