READS=$1
ncbi-blast-2.6.0+/bin/blastn -num_threads 4 -outfmt "17 SQ SR qseqid sseqid std" -query $READS -out $2 -task blastn -evalue=10e4 -db $3
