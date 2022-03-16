# EGG_and_mouse_tracking
Code used for running experiment using both mouse-tracking and EEG.

### TO DO
    - [ ] Set up experimental trials as well
    - [ ] Add please start moving if no mouse-movement is detected within 1 second (60 Hz)
    - [ ] Potentially save mouse positions and timestamps as a list in accuracy dataframe would be better?

    - [X] When done make buttons transparent   
    - [X] Check how file looks when including both experimental and practise trials
    - [X] Check that we can use the mousetrap package in R 
    - [X] Await trigger from scanner
    - [X] Fix discrepancy between buttons and where it works to click wtf??? (solution: use windowsss )
    - [X] Fix quit keys
    - [X] Put right triggers in the right places    
    - [X] Decide when the mouse should return to original position (maybe when images are shown?) - otherwise you can move the mouse beforehand
    - [X] Fill out structure in the beginning of .py file
    - [X] Calculate reaction time
    - [X] End trial when you click on either of the botton    
    - [X] Should if frame == 1 be changed to 0? No it should not
    - [X] Fix merged dataframe
        - [-] Calculate velocity of mouse (Not needed seems we can use the mousetrap package in R)
    - [X] Better file name
    - [-] If no click, then empty string in columns for accuracy dataframe (not needed already empty)
    - [X] Decide on duration for fixation
    - [X] Check that right and left img + buttons are in the right places
    - [X] Figure out how to repeat three times
    - [X] Decide on max length of trial and change it
    - [X] Display intro text