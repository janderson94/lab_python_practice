#This script will summarize a GTF file in a variety of ways
import os
from os.path import expanduser

home=expanduser("~")

#Get average length
dict1={}
dict2={}
with open(home + "/Desktop/panubis1.gtf","r") as file:
    for line in file:
        l2=line.strip().split("\t")
        if l2[0][0] =='#':
            continue
        elif l2[2] in dict2:
            dict1[l2[2]] += (int(l2[4])-int(l2[3]) + 1)
            dict2[l2[2]] += 1
            continue

        elif l2[2] in ['gene','exon','CDS','start_codon','stop_codon']:
            dict1[l2[2]] = (int(l2[4])-int(l2[3]) + 1)
            dict2[l2[2]] = 1

for key in dict1:
	print(key, dict1[key]/(dict2[key]))

#It looks like some of our start/stop codons aren't 3 basepairs.
#Exons are ~300BP on average, which makes sense
#Genes are around 37KB
