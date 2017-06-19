python filtre_aln.py $1
python couverture_horizontale.py $SAM
python couverture_verticale.py $SAM
SAM=new_$1
BAM=${SAM%%.*}.bam
SORTED_BAM=${SAM%%.*}_sorted.bam
INDEX=${SAM%%.*}_sorted.bai
/home/athomas/samtools/samtools view -bT /home/athomas/aster/Mus_musculus.GRCm38.cdna.all.fa $SAM > $BAM
/home/athomas/samtools/samtools sort $BAM -o $SORTED_BAM
/home/athomas/samtools/samtools index $SORTED_BAM $INDEX
echo "Nombre de reads :"
/home/athomas/samtools/samtools idxstats $SORTED_BAM | awk '{s+=$3+$4} END {print s}'
echo "Nombre de reads mappés :"
/home/athomas/samtools/samtools idxstats $SORTED_BAM | awk '{s+=$3} END {print s}'

