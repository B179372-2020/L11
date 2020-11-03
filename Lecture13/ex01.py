#!/usr/bin/python3

#data = open("data.csv","w")
#dmeef main():
with open ("data.csv") as data:
	for line in data:
		line_list = line.split(",")
		#print(line_list)
		gene_name = line_list[2]
		print(gene_name)
		
		seq = line_list[1]
		#print(len(seq))
		print(seq[89:110])
		
		at_content = (seq.count("a")+seq.count("t"))/len(seq)
		if float(at_content) < 0.5:
			print(gene_name,"AT content is less than 0.5")
		if int(line_list[3]) >200:
			print(gene_name,"expression level is greater than 200")

		
		if gene_name.startswith('k') or gene_name.startswith('h'):
			if line_list[0].endswith('s'):
				print(gene_name,'begins with "k" or "h" except those belonging to Drosophila melanogaster')

		
		if at_content >= 0.65:
			print(gene_name,':AT content is high\n')
		elif at_content < 0.65 and at_content > 0.45:
			print(gene_name,':AT content is medium\n')
		else:
			print(gene_name,':AT content is low\n')

