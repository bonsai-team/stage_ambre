#!/bin/bash

#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --time=36:00:00
#SBATCH --job-name=sortme_alnCB
#SBATCH --mem=36G

./sortmedna --ref ../combined.filtered.fa,musdb --reads ../reads_CB.filtered.fasta --aligned sortme_aln_CB --sam
