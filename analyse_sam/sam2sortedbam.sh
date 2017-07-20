python filtre_aln.py $1
SAM=new_$1
python couverture.py $SAM
BAM=${SAM%%.*}.bam
SORTED_BAM=${SAM%%.*}_sorted.bam
INDEX=${SAM%%.*}_sorted.bai
samtools view -bT $2 $SAM > $BAM

samtools flagstat $BAM
samtools sort $BAM -o $SORTED_BAM
samtools index $SORTED_BAM $INDEX
