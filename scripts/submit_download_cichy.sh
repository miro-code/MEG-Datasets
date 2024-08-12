#! /bin/bash
#SBATCH --nodes=1
#SBATCH --job-name=download_cichy
#SBATCH --time=168:00:00
#SBATCH --partition=long
#SBATCH --account=engs-pnpl
#SBATCH --output=results/slurm_out/%j.out

echo "Downloading Cichy 2016 data"
sh Cichy2016/download_cichy.sh