#!/bin/usr/python3


#First want to start a dictionary with E1-E15 and the associated length
out={}
for f in range(1,16):
    out['E'+str(f)]=0




with open('./E062_15_coreMarks_hg38lift_segments.bed') as bed:
    for line in bed:
        l2=line.strip().split("\t")
        out[l2[3]]= out[l2[3]] + (int(l2[2])-int(l2[1]))


#write out as tab delimited
f=open('segment_combined_lengths.txt',"w")
for key,val in out.items():
    f.write('%s %s\n' % (key, val))

f.close()
