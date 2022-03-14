# EGG_and_mouse_tracking
Code used for running experiment using both mouse-tracking and EEG.

### TO DO
    - [ ] Display intro text and await trigger from scanner
    - [ ] Put right triggers in the right places
        - [ ] Trigger for clicking?
    - [ ] Check that right and left img + buttons are in the right places
        - [ ] When done make buttons transparent
    - [ ] Decide on duration for fixation
    - [ ] Set up experimental trials as well
        - [ ] Figure out how to repeat three times (do we just copy and paste in the csv-file or is there a smart code implementation)
    - [ ] Decide on max length of trial and change it 
    - [ ] Fix quit keys
    - [ ] Fix discrepancy between buttons and where it works to click wtf???
    - [ ] Check how file looks when including both experimental and practise trials
    - [ ] Check that we can use the mousetrap package in R

    - [X] Decide when the mouse should return to original position (maybe when images are shown?) - otherwise you can move the mouse beforehand
    - [X] Fill out structure in the beginning of .py file
    - [X] Calculate reaction time
    - [X] End trial when you click on either of the botton    
    - [X] Should if frame == 1 be changed to 0? No it should not
    - [X] Fix merged dataframe
        - [-] Calculate velocity of mouse (Not needed seems we can use the mousetrap package in R)
    - [X] Better file name
    - [-] If no click, then empty string in columns for accuracy dataframe (not needed already empty)