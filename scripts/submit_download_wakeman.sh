#! /bin/bash
#SBATCH --nodes=1
#SBATCH --job-name=download_wakeman
#SBATCH --time=48:00:00
#SBATCH --partition=medium
#SBATCH --account=engs-pnpl
#SBATCH --output=results/slurm_out/%j.out

echo "Downloading Wakeman 2021 data"
python Wakeman2021/download_wakeman.py