#!/bin/bash

#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --time=06:00:00
#SBATCH --job-name=sortme_index
#SBATCH --mem=20G

./indexdb_dna --ref ../combined.filtered.fa,musdb --sensitive -v --tmpdir index
