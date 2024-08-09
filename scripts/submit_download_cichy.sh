#! /bin/bash
#SBATCH --nodes=1
#SBATCH --job-name=download_data
#SBATCH --time=48:00:00
#SBATCH --partition=medium
#SBATCH --account=engs-pnpl
#SBATCH --output=results/slurm_out/%j.out

echo "Downloading Cichy 2016 data"
sh Cichy2016/download_cichy.sh