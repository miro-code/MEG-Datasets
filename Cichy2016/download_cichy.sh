mkdir MEG1
cd MEG1
wget -r -np -nH --cut-dirs=2 -R "index.html*" http://wednesday.csail.mit.edu/MEG1_MEG_Clear_Data/
wget -r -np -nH --cut-dirs=2 -R "index.html*" http://wednesday.csail.mit.edu/MEG1_MEG_Epoched_Raw_Data/
wget -r -np -nH --cut-dirs=2 -R "index.html*" http://wednesday.csail.mit.edu/MEG1_fMRI_Clear_Data/
cd .. 
mkdir MEG2
cd MEG2
wget http://userpage.fu-berlin.de/rmcichy/Khaligh_Razavi_et_al_2018JoCN/118_visual_stimuli.mat
wget -r -np -nH --cut-dirs=2 -R "index.html*" http://wednesday.csail.mit.edu/MEG2_MEG_Clear_Data/
wget -r -np -nH --cut-dirs=2 -R "index.html*" http://wednesday.csail.mit.edu/MEG2_MEG_Epoched_Raw_Data/
wget -r -np -nH --cut-dirs=2 -R "index.html*" http://wednesday.csail.mit.edu/MEG2_fMRI_Clear_Data/