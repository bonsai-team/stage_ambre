#!/bin/bash

#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --time=24:00:00
#SBATCH --job-name=graphmap_CB
#SBATCH --mem=24G

./graphmap align -r ../combined.filtered.fa -d ../BYK_CB_ONT_1_FAF04998_A_1Donly.fastq -o graphmap_CB.sam
