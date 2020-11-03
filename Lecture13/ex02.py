#!/usr/bin/python3

input_seqs = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']
for_range = list(range(0,len(input_seqs)))    ### [0, 1, 2, 3]

for Xaxis_item in for_range:
	first_query = list(input_seqs[Xaxis_item])
	for Yaxis_item in for_range:
		distance = 0
		other_query = list(input_seqs[Yaxis_item])
		for base in list(range(0,len(first_query))):
             		print("Index" + str(base) + ":" +str(first_query[base]) + "," + str(other_query[base]) + "...")
             		if first_query[base] == other_query[base]:
                  		distance = distance + 1
		print(str(distance))
		print("\t" + str(int(100*(distance/len(input_seqs[Xaxis_item])))))
