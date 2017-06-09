#!/bin/bash

#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --time=24:00:00
#SBATCH --job-name=graphmap_DB
#SBATCH --mem=24G

./graphmap align -r ../combined.filtered.fa -d ../BYK_DB_ONT_1_FAF05081_A_1Donly.fastq -o graphmap_DB.sam
