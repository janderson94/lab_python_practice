#Generate CpG shore intervals surrounding CpG islands
n =open('panubis_cpg_shores.bed',"a")

with open('panubis_cpg_island.bed') as f:
    for line in f:
        cols = line.strip('\n').split('\t')
        n.write(cols[0]+"\t"+ (str(0) if((int(cols[1])-2000)<0) else str((int(cols[1])-2000)))+"\t"+cols[1])
        n.write("\n")
        n.write(cols[0]+"\t"+ cols[2]+ "\t" + str(int(cols[2])+2000))
        n.write("\n")


n.close()


n =open('panubis_cpg_shores.bed',"a")

with open('panubis_cpg_island.bed') as f:
    for line in f:
        cols = line.strip('\n').split('\t')
        n.write(cols[0]+"\t"+ (str(0) if((int(cols[1])-2000)<0) else str((int(cols[1])-2000)))+"\t"+cols[1]+"\n")
        n.write(cols[0]+"\t"+ cols[2]+ "\t" + str(int(cols[2])+2000)+"\n")



n.close()
