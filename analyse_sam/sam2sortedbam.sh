#python filtre_aln.py $1
SAM=new_$1
python couverture_horizontale.py $SAM
python couverture_verticale.py $SAM
BAM=${SAM%%.*}.bam
SORTED_BAM=${SAM%%.*}_sorted.bam
INDEX=${SAM%%.*}_sorted.bai
/home/athomas/samtools/samtools view -bT /home/athomas/aster/Mus_musculus.GRCm38.cdna.all.fa $SAM > $BAM
#/home/athomas/samtools/samtools fixmate -r $BAM -O sam test.sam
#/home/athomas/samtools/samtools view -bT /home/athomas/aster/Mus_musculus.GRCm38.cdna.all.fa test.sam > test.bam
#/home/athomas/samtools/samtools flagstat test.bam
/home/athomas/samtools/samtools flagstat $BAM
/home/athomas/samtools/samtools sort $BAM -o $SORTED_BAM
/home/athomas/samtools/samtools index $SORTED_BAM $INDEX
echo "Nombre de reads :"
/home/athomas/samtools/samtools idxstats $SORTED_BAM | awk '{s+=$3+$4} END {print s}'
echo "Nombre de reads mappés :"
/home/athomas/samtools/samtools idxstats $SORTED_BAM | awk '{s+=$3} END {print s}'
../../qualimap_v2.2.1/qualimap bamqc -bam $SORTED_BAM -nt 2 -outfile ${SORTED_BAM%%.*} --java-mem-size=4G

