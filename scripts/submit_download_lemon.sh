#! /bin/bash
#SBATCH --nodes=1
#SBATCH --job-name=download_lemon
#SBATCH --time=48:00:00
#SBATCH --partition=medium
#SBATCH --account=engs-pnpl
#SBATCH --output=results/slurm_out/%j.out

echo "Downloading Lemon 2018 data"
sh Lemon2018/download_lemon.sh