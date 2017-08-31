READS=$1
ncbi-blast-2.6.0+/bin/makeblastdb -dbtype nucl -in $READS -title ${READS%%.*} -out ${READS%%.*} -parse_seqids
