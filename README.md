# EEG_and_mouse_tracking
This repository holds the code used for running mouse-tracking and EEG experiment and analysing the data. The code was used for the exam project in Cognitive Neuroscience. 


### Experimental design
The participant is exposed to a object discrimination task, in which two stimulus objects are presented. Before each trial, the participant is instructed to press on a certain stimulus (for example “banana”). Three types of trials are presented:
1. A congruent trial, in which stimulus objects are colored congruently with their typical color (e.g., a yellow banana and a red apple). 
2. An incongruent trial, in which the colors of stimulus object are switched (e.g., a yellow apple, and a red banana)
3. A neutral trial, in which the stimulus objects consist of achromatic line drawings of the stimulus objects. 


### Code overview
| File                               | Purpose                                                           |
| ---------------------------------- | ------------------------------------------------------------------|
| `ICA.ipynb`                        | Cleaning data and creating epochs for further analysis            |
| `time_frequency.ipynb` | Time frequency analysis of EEG signal (Cluster-based permutation test and plotting|
| `mousetracking_EEG_behavioural.py` | Code for running the experiment without EEG triggers              |
| `mousetracking_EEG.py`             | Code for running the experiment with EEG triggers                 |
| `mousetrack_analysis.Rmd`          | Analysis of mouse-tracking data                                   |