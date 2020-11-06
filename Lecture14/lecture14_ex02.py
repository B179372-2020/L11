#!/usr/bin/python3

def percentage(pro_seq,aa_residue="aILMFWYV"):
	aa_residue = list(aa_residue)
	aalist_length = len(aa_residue)
	aa_number = list(range(aalist_length))
	for i in range(aalist_length): 
		aa_number[i] = pro_seq.upper().count(aa_residue[i].upper())
	percentage = sum(aa_number)/len(pro_seq)*100
	print(aa_number,percentage)
	
#percentage("MSRSLLLRFLLFLLLLPPLP",["M"])
#percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])

percentage("MSRSLLLRFLLFLLLLPPLP")
#assert round(percentage("MSRSLLLRFLLFLLLLPPLP")) == 65
