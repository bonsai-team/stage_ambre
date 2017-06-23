python filtre_aln.py $1
SAM=new_$1
python couverture_horizontale.py $SAM
BAM=${SAM%%.*}.bam
SORTED_BAM=${SAM%%.*}_sorted.bam
INDEX=${SAM%%.*}_sorted.bai
/home/athomas/samtools/samtools view -bT /home/athomas/aster/Mus_musculus.GRCm38.cdna.all.fa $SAM > $BAM

#SAM_no_secondary=${SAM%%.*}_test.sam
#/home/athomas/samtools/samtools fixmate -r $BAM -O sam $SAM_no_secondary
#BAM_no_secondary=${SAM_no_secondary%%.*}.bam
#/home/athomas/samtools/samtools view -bT /home/athomas/aster/Mus_musculus.GRCm38.cdna.all.fa $SAM_no_secondary > $BAM_no_secondary
#/home/athomas/samtools/samtools flagstat $BAM_no_secondary
/home/athomas/samtools/samtools flagstat $BAM
#BAM_sorted_no_secondary=${BAM_no_secondary%%.*}_sorted.bam
#/home/athomas/samtools/samtools sort $BAM_no_secondary -o $BAM_sorted_no_secondary
#INDEX_no_secondary=${BAM_sorted_no_secondary%%.*}.bai
#/home/athomas/samtools/samtools index $BAM_sorted_no_secondary $INDEX_no_secondary
/home/athomas/samtools/samtools sort $BAM -o $SORTED_BAM
/home/athomas/samtools/samtools index $SORTED_BAM $INDEX
echo "Nombre de reads :"
/home/athomas/samtools/samtools idxstats $SORTED_BAM | awk '{s+=$3+$4} END {print s}'
#/home/athomas/samtools/samtools idxstats $BAM_sorted_no_secondary | awk '{s+=$3+$4} END {print s}'
echo "Nombre de reads mappés :"
/home/athomas/samtools/samtools idxstats $SORTED_BAM | awk '{s+=$3} END {print s}'
#/home/athomas/samtools/samtools idxstats $BAM_sorted_no_secondary | awk '{s+=$3} END {print s}'
../../qualimap_v2.2.1/qualimap bamqc -bam $SORTED_BAM -nt 2 -outfile ${SORTED_BAM%%.*} --java-mem-size=4G
#../../qualimap_v2.2.1/qualimap bamqc -bam $BAM_sorted_no_secondary -nt 2 -outfile ${BAM_sorted_no_secondary%%.*} --java-mem-size=4G
