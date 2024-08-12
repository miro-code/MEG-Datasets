#!/bin/bash

cd ../../datasets
mkdir -p Lemon2018
cd Lemon2018

FTP_URL="https://ftp.gwdg.de/pub/misc/MPI-Leipzig_Mind-Brain-Body-LEMON/"

wget -c -r -np -nH --cut-dirs=4 -R "index.html*" $FTP_URL


