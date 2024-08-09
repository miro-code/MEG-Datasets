import os
import subprocess
import argparse

# Parse arguments
parser = argparse.ArgumentParser(description='Download and unpack dataset')
parser.add_argument('--target_path', type=str, required=True,
                    help='Target path for downloading and unpacking the dataset')
parser.add_argument('--repo_url', type=str, required=True,
                    help='URL of the Git repository to clone')
args = parser.parse_args()

# run this script with the following command:
# python download_git_annex_dataset.py --target_path /Lemon2018 --repo_url https://github.com/OpenNeuroDatasets/ds000221.git


def run_command(command):
    """
    Execute a shell command in a subprocess, and print the output.
    """
    try:
        result = subprocess.run(command, check=True,
                                text=True, capture_output=True)
        print(result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.stderr}")
        return None


def clone_and_setup_annex(repo_url, clone_to):
    """
    Clone a Git repository and set up git-annex.
    """
    # Ensure the directory exists and is empty
    print(f"Cloning {repo_url} into {os.getcwd()} / {clone_to}...")
    os.makedirs(clone_to, exist_ok=True)
    if len(os.listdir(clone_to)) != 0:
        print(f"Directory {clone_to} is not empty. Cloning skipped.")
        return

    # Clone the repository
    print(f"Cloning {repo_url} into {clone_to}...")
    clone_result = run_command(['git', 'clone', repo_url, clone_to])

    if clone_result is not None:
        # Initialize git-annex
        os.chdir(clone_to)  # Change working directory to the repo
        print("Initializing git-annex...")
        run_command(['git', 'annex', 'init'])

        # Get all files or specific files
        print("Retrieving data with git-annex...")
        # Retrieves all files; customize as needed
        run_command(['git', 'annex', 'get', '.'])


# make /arc_data working directory
os.chdir(os.path.join("/", "arc_data", "MEG-Datasets", "LemonData"))

# print list of files in /arc_data/MEG-Datasets
print("Files in /arc_data/MEG-Datasets:")
print(os.listdir())


clone_and_setup_annex(args.repo_url, args.target_path)
