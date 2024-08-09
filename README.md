# MEG-Datasets

Scripts for downloading MEG Datasets from public sources.

# Download Data
Some of the download scripts requires git-annex to be installed. On ARC this is not possible. Therefore, I provide a Dockerfile that can be used to build a singularity. If my directory /data/engs-pnpl/trin4076/ is still around you might not need to build your own. Just execute sbatch submit_download_lemon.sh. Otherwise you have to build a singularity. Install docker and apptainer. Build the docker-image with "docker build --platform linux/amd64 -t <DockerUsername>/download_lemon .". Push it docker push <DockerUsername>/download_lemon. Then use apptainer apptainer build /tmp/lima/download_lemon.sif docker:// <DockerUsername>/download_lemon. Then do "mv /tmp/lima/download_lemon.sif ~/MEG-Datasets/Lemon2018". The lima stuff is mac specific you might want to change it if you are on a different OS. The resulting sif can be executed with the submit_download_data.sh script.