#!/bin/sh

#SBATCH --account=impd
#SBATCH --time=00:20:00
#SBATCH --job-name=anim_sd
#SBATCH -o %j_log.out
#SBATCH --error=%j_err.err
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=butzer@contractor.usgs.gov

source /home/butzer/miniconda3/bin/activate nlcd2

python3 anim.py 15_05_2022
#python3 anim.py 15_06_2022
