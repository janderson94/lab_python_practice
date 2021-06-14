import numpy as np
import os
import re


files = os.popen("ls ./unfiltered_medaka/").read().strip().split("\n")

with open('./loci.txt') as l:
    loci=l.read().splitlines()


out = np.zeros(shape=(len(loci),len(files)))

nfile=1
for f in files:
    with open("./unfiltered_medaka/"+f,"r") as sample:
        for line in sample:
            if line[0]=="#":
                continue
            line=line.strip().split("\t")
            nloci=1
            for locus in loci:
                if (line[0]==locus.split("_")[0] and line[1]==locus.split("_")[1]):
                    out[nloci-1,nfile-1] = line[5]
                nloci += 1
        nfile+=1

np.savetxt("coverage_medaka_by_locus_and_sample.txt",out)

#Same thing but actually pull genotypes
out = np.zeros(shape=(len(loci),len(files)))
out[out==0]= (-1)

nfile=1
for f in files:
    with open("./unfiltered_medaka/"+f,"r") as sample:
        for line in sample:
            if line[0]=="#":
                continue
            line=line.strip().split("\t")
            nloci=1
            for locus in loci:
                if (line[0]==locus.split("_")[0] and line[1]==locus.split("_")[1] and line[9]!='.'):
                    text=line[9]
                    out[nloci-1,nfile-1] = int(line[9].split(":")[0].split("/")[0])+int(line[9].split(":")[0].split("/")[1])
                nloci += 1
        nfile+=1

np.savetxt("genotype_medaka_by_locus_and_sample.txt",out)
