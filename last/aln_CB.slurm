#!/bin/bash

#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --time=24:00:00
#SBATCH --job-name=lastal_CB
#SBATCH --mem=64G

lastal -v -Q 1 -P 8 -p train_CB.par musdb ../BYK_CB_ONT_1_FAF04998_A_1Donly.fastq > last_CB.maf
