import pysam
import numpy as np
import os

with open('../targeted_flongle_sites_oct20.bed') as f:
    lines=f.read().splitlines()

#Output matrix is N regions by M samples
files = os.popen("ls ./aligned_sam/*.bam").read().strip().split("\n")

#Great now have an N region by M sample matrix to store counts if they map within a region
#index by region and file

out = np.zeros(shape=(len(lines),len(files)))

f=1
#iterate across files and read them in one by one
for sample in files:
    samfile = pysam.AlignmentFile(sample, "rb")
    l=1
    #For each target region, count the number of reads mapping within for this file
    for region in lines:
        #Split region into readable format
        r2 = region.strip().split("\t")
        count=0
        #Fetch reads
        for read in samfile.fetch(r2[0],int(float(r2[1])),int(float(r2[2]))):
            count += 1
        #Store all reads mapping from a given sample to that region
        out[l-1,f-1]=count
        l += 1
    print("Processing sample",sample)
    f += 1

np.savetxt("coverage_by_region_and_sample.txt",out)
