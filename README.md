# EEG_and_mouse_tracking
This repository holds the code used for running and analysing experiment using a combination of mouse-tracking and EEG.


### Code overview
| File                               | Purpose                   |
| ---------------------------------- | ------------------------- |
| `ICA.ipynb`                        | Analysis of EEG data using the `mne`-package in Python            |
| `mousetrack_analysis.Rmd`          | Analysis of mousetracking data using the `mousetrap`-package in R |
| `mousetracking_EEG.py`             | Code for running the experiment with EEG triggers                 |
| `mousetracking_EEG_behavioural.py` | Code for running the experiment without EEG triggers              |