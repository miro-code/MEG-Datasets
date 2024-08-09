#! /bin/bash
#SBATCH --nodes=1
#SBATCH --job-name=download_data
#SBATCH --time=00:10:00
#SBATCH --partition=devel
#SBATCH --account=engs-pnpl
#SBATCH --output=results/slurm_out/%j.out

echo "Downloading Lemon 2018 data"
echo "DATA: $DATA"
singularity run -B $DATA:/arc_data /data/engs-pnpl/trin4076/MEG-Datasets/Lemon2018/download_lemon.sif