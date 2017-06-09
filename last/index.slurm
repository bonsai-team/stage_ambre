#!/bin/bash

#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --time=06:00:00
#SBATCH --job-name=last_index
#SBATCH --mem=20G

lastdb -v musdb ../combined.filtered.fa
