#!/bin/bash

#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --time=06:00:00
#SBATCH --job-name=bwa-mem_index
#SBATCH --mem=20G

./bwa index ../combined.filtered.fa
