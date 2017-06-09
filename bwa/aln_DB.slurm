#!/bin/bash

#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --time=24:00:00
#SBATCH --job-name=bwa_DB
#SBATCH --mem=32G

./bwa mem -x ont2d ../combined.filtered.fa ../BYK_DB_ONT_1_FAF05081_A_1Donly.fastq > bwa_aln_DB.sam
