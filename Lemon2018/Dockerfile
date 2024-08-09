FROM ubuntu:22.04
# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get install -y git
RUN apt-get install -y git-annex

# install app
COPY download_git_annex_dataset.py /

# run app
ENTRYPOINT sh -c 'python3 /download_git_annex_dataset.py --target_path Lemon2018 --repo_url https://github.com/OpenNeuroDatasets/ds000221.git'