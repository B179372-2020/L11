#!/usr/bin/python3

def percentage(pro_seq,aa_residue):
	aa_number = pro_seq.upper().count(aa_residue.upper())
	total_length = len(pro_seq)
	percentage = aa_number / total_length
	return(percentage)
print(percentage("MSRSLLLRFLLFLLLLPPLP","M"))


#assert round(percentage("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
#assert round(percentage("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
#assert round(percentage("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
#assert round(percentage("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
