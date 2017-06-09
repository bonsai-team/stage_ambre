#!/bin/bash

#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --time=24:00:00
#SBATCH --job-name=lastal_DB
#SBATCH --mem=64G

lastal -v -Q 1 -P 8 -p train_DB.par musdb ../BYK_DB_ONT_1_FAF05081_A_1Donly.fastq > last_DB.maf
