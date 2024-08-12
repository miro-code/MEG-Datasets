import os
import argparse
import urllib.request
import zipfile

#  This file should download wakeman "in a non-BIDS format (which may be easier to download by subject rather than by modality"

# Parse arguments
parser = argparse.ArgumentParser(description='Download and unpack dataset')
parser.add_argument('--target_path', type=str, default=os.path.abspath(os.path.join(
    os.getcwd(), os.pardir, "Wakeman2021")), help='Target path for downloading and unpacking the dataset')
args = parser.parse_args()

# Create the path if it does not exist
target_path = args.target_path
if not os.path.exists(target_path):
    os.makedirs(target_path)


urls = [
    "https://s3.amazonaws.com/openneuro/ds000117/ds000117_R1.0.0/compressed/ds000117_R1.0.0_derivatives_sub01-04.zip",
    "https://s3.amazonaws.com/openneuro/ds000117/ds000117_R1.0.0/compressed/ds000117_R1.0.0_derivatives_sub05-08.zip",
    "https://s3.amazonaws.com/openneuro/ds000117/ds000117_R1.0.0/compressed/ds000117_R1.0.0_derivatives_sub09-12.zip",
    "https://s3.amazonaws.com/openneuro/ds000117/ds000117_R1.0.0/compressed/ds000117_R1.0.0_derivatives_sub13-16.zip",
    "https://s3.amazonaws.com/openneuro/ds000117/ds000117_R1.0.0/compressed/ds000117_R1.0.0_metadata.zip",
    "https://s3.amazonaws.com/openneuro/ds000117/ds000117_R1.0.0/compressed/ds000117_R1.0.0_mriqc.zip",
    "https://s3.amazonaws.com/openneuro/ds000117/ds000117_R1.0.0/compressed/ds000117_R1.0.0_sourcedata.zip",
    "https://s3.amazonaws.com/openneuro/ds000117/ds000117_R1.0.0/compressed/ds000117_R1.0.0_stimuli.zip",
    "https://s3.amazonaws.com/openneuro/ds000117/ds000117_R1.0.0/compressed/ds000117_R1.0.0_sub01-04.zip",
    "https://s3.amazonaws.com/openneuro/ds000117/ds000117_R1.0.0/compressed/ds000117_R1.0.0_sub05-08.zip",
    "https://s3.amazonaws.com/openneuro/ds000117/ds000117_R1.0.0/compressed/ds000117_R1.0.0_sub09-12.zip",
    "https://s3.amazonaws.com/openneuro/ds000117/ds000117_R1.0.0/compressed/ds000117_R1.0.0_sub13-16.zip",
]

# Download and unpack data
for url in urls:
    file_name = os.path.join(target_path, os.path.basename(url))
    print(f'Downloading {url} to {file_name}')
    urllib.request.urlretrieve(url, file_name)

    print(f'Unpacking {file_name}')
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(target_path)

print('Download and unpacking completed.')
