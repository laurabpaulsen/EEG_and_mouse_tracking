""" DESCRIPTION:
This combined EEG and mouse tracking experiment displays two stimuli on either side of the screen. Before this presentation a word indicates what the participant should click on. The stimuli can either be neutral (line-drawings), color congruent, or color incongruent (color of stimuli switched around). 
The experiment lasts around 10 minutes and has 172 trials (including practice trials)
/Code written by Laura Bock Paulsen 2022, adapted from a OpenSesame experiment by Jessica Clarke and Sille Hasselbalch.
/Code inspired by Mikkel Wallentin & Roberta Rocca 2019

Structure:  
    GET PARTICIPANT INFO USING GUI
    PREPARE LOG FILES
    SPECIFY TIMING AND MONITOR
    LOADING IN EXPERIMENTAL DETAILS
    FUNCTION FOR EXPERIMENTAL LOOP
    DISPLAY INTRO TEXT AND AWAIT SCANNER TRIGGER
    CALL FUNCTION RUNNING THE EXPERIMENTAL LOOP
    

"""


# Import the modules that we need in this script
from __future__ import division
from psychopy import core, visual, event, gui, monitors, event
import pandas as pd
#from triggers import setParallelData
from datetime import datetime
import csv


# Monitor parameters
MON_DISTANCE = 60  # Distance between subject's eyes and monitor 
MON_WIDTH = 20  # Width of your monitor in cm
MON_SIZE = [1440, 900]  # Pixel-dimensions of your monitor
FRAME_RATE = 60 # Hz
SAVE_FOLDER = 'Stroop_mouse_EEG_data/'  # Log is saved to this folder. 

"""
GET PARTICIPANT INFO USING GUI
"""
# Intro-dialogue. Get subject-id and other variables.
# Save input variables in "V" dictionary (V for "variables")
V = {'ID':'','gender':['female','male','other'],'age':''}
if not gui.DlgFromDict(dictionary = V, title = 'EEG and Mousetracking Experiment').OK: # dialog box; order is a list of keys 
    core.quit()

'''
PREPARE LOG FILES
'''
now = datetime.now()
utc_time = now.strftime("%H_%M_%S")

filename =  str(SAVE_FOLDER) + str(V['ID']) + str(utc_time) + '.csv'

list_of_columns = ['ID', 'age', 'gender', 'word', 'category', 'word_trigger','condition_trigger','right_img', 'left_img','img_trigger','onset_word', 'onset_img', 'correct_resp','trial_type','trial_number', 'ypos', 'xpos', 'rt', 'offset_word', 'key_t', 'offset_img', 'response', 'condition_trigger_t', 'accuracy', 'phase', 'trial_timestamp', 'click_trigger']
csvfile = open(filename,'w', newline='')
writer = csv.DictWriter(csvfile, fieldnames = list_of_columns)
writer.writeheader()


filename2 = str(SAVE_FOLDER)+ 'accuracy_' + str(V['ID']) + str(utc_time) + '.csv'
csvfile2 = open(filename2,'w', newline='')
writer2 = csv.DictWriter(csvfile2, fieldnames = list_of_columns)
writer2.writeheader()
"""
SPECIFY TIMING AND MONITOR
"""

# Clock and timer
clock = core.Clock()  # A clock wich will be used throughout the experiment to time events on a trial-per-trial basis (stimuli and reaction times).

# Create psychopy window
my_monitor = monitors.Monitor('testMonitor', width=MON_WIDTH, distance=MON_DISTANCE)  # Create monitor object from the variables above. This is needed to control size of stimuli in degrees.
my_monitor.setSizePix(MON_SIZE)
win = visual.Window(monitor = my_monitor, units = 'deg', fullscr=True, allowGUI=True, color='black')  # Initiate psychopy Window as the object "win", using the myMon object from last line. Use degree as units!

# Prepare Fixation cross
stim_fix = visual.TextStim(win, '+', alignText = 'center')
stim_fix_low = visual.TextStim(win, '+', pos=[0.0, -1.1]) # FIX THIS SHIT

'''
LOADING IN EXPERIMENTAL DETAILS
'''
# Load in csv's with details about trials
practisedf = pd.read_csv('trial_info/practisetrials.csv', sep = ';')
experimentaldf = pd.read_csv('trial_info/experimentaltrials.csv', sep = ';')

# Randomizing the order of the rows in the practise df
practisedf = practisedf.sample(frac=1).reset_index(drop=True)
experimentaldf = experimentaldf.sample(frac=1).reset_index(drop=True)
experimentaldf = pd.concat([experimentaldf]*3, ignore_index=True) # Running the experimental trials three times

# The word stimulus 
stim_text = visual.TextStim(win=win, pos=[0,0], height=0.7, alignText='center')

# The image size and position using ImageStim, file info added in trial list below.

stim_left_pos = (-5.5, 3)
stim_right_pos = (5.5, 3)
stim_size = (7, 5)


stim_image_left = visual.ImageStim(win,
    mask=None,
    pos=stim_left_pos,
    size=stim_size,
    ori=1)

stim_image_right = visual.ImageStim(win,
    mask=None,
    pos=stim_right_pos,
    size=stim_size,
    ori=1)

button_left = visual.Rect(win, size = stim_size, pos = stim_left_pos, fillColor = 'blue', opacity = 0.2)
button_right = visual.Rect(win, size = stim_size, pos = stim_right_pos, fillColor = 'red', opacity = 0.2)

# Use these instead if using mac with retina - for some reason there is a discrepancy between the measured mouselocation and where the stimuli is shown
#button_left = visual.Rect(win, size = (12,9.5), pos = (10,5), fillColor = 'green', opacity = 0.3)
#button_right = visual.Rect(win, size = (-12,9.5), pos = (-10,5), fillColor = 'yellow', opacity = 0.3)



# Mouse
mouse = event.Mouse(visible=True, win=win)

KEYS_QUIT = ['escape','q']  # Keys that quits the experiment
KEYS_trigger=['t'] # The MR scanner sends a "t" to notify that it is starting

MAX_LENGTH_TRIAL = 500 # The maximum number of frames in each trial


'''
FUNCTION FOR EXPERIMENTAL LOOP
'''
def make_trial_list(trial_df):
    trial_list = []
    
    for i in range(len(trial_df)):
        data = trial_df.loc[i]
        if data['trial_type'] == 'neutral':
            TRIG_C = 10
            TRIG_I = 11
            TRIG_W = 12
        if data['trial_type'] == 'congruent':
            TRIG_C = 20
            TRIG_I = 21
            TRIG_W = 22
        if data['trial_type'] == 'incongruent':
            TRIG_C = 30
            TRIG_I = 31
            TRIG_W = 32
        # Add a dictionary for every trial
        trial_list += [{
            'ID': V['ID'],
            'age': V['age'],
            'gender': V['gender'],
            'word':data['task'],
            'category':data['category'],
            'word_trigger':TRIG_W,
            'condition_trigger':TRIG_C,
            'condition_trigger_t':'',
            'right_img': data['right_image'],
            'left_img': data['left_image'],
            'img_trigger':TRIG_I,
            'onset_word':'',
            'offset_word': '',
            'onset_img':'',
            'offset_img': '',
            'response': '',
            'key_t':'',
            'rt': '',
            'correct_resp': data['correct_response'],
            'accuracy': '',
            'trial_type':data['trial_type'],
            'trial_number': i + 1,
            'phase': data['phase'],
            'trial_timestamp': ''
        }]
    return trial_list



def run_experiment(trial_list, exp_start):
    """
    Runs a block of trials. This is the presentation of stimuli,
    collection of responses and saving the trial
    """

    #Set EEG trigger in off state
    pullTriggerDown = False
    # Loop over trials
    for trial in trial_list:
        mouse.setPos(newPos = [0.0, -9])
        event.clearEvents()# clear input to make sure that no responses are logged that do not belong to stimulus
        
        # prepare word
        stim_text.text = trial['word']
        print(stim_text.text)
        time_flip_word = core.monotonicClock.getTime() #onset of stimulus

        for frame in range(60):
            stim_text.draw()
            if frame==1:
                #win.callOnFlip(setParallelData, trial['word_trigger']) 
                pullTriggerDown = True

            win.flip()

            if pullTriggerDown:
                #win.callOnFlip(setParallelData, 0)
                pullTriggerDown = False

        # Display fixation cross
        for frame in range(12):
            stim_fix_low.draw()

        # Prepare images
        stim_image_right.image = trial['right_img']
        stim_image_left.image = trial['left_img']


        # Display images and monitor time + ensure mouse starts in the same place
        mouse.setPos(newPos = [0.0, -9])
        time_flip_img = core.monotonicClock.getTime() #onset of stimulus
        for frame in range(MAX_LENGTH_TRIAL):
            stim_image_right.draw()
            stim_image_left.draw()
            button_right.draw()
            button_left.draw()
            button_click_right.draw()
            button_click_left.draw()

            if frame==1:
                #win.callOnFlip(setParallelData, trial['img_trigger'])  # pull trigger up
                pullTriggerDown = True
            win.flip()
            if pullTriggerDown:
                #win.callOnFlip(setParallelData, 0)
                pullTriggerDown = False

            #Log values
            trial['onset_word'] = time_flip_word-exp_start
            trial['onset_img'] = time_flip_img-exp_start
            #trial['pause_trigger_t']=pause_trigger_t-exp_start

            #Log values for mouse
            trial['xpos'] = mouse.getPos()[0]
            trial['ypos'] = mouse.getPos()[1]

            #Log trial timestamp
            time_trial = core.monotonicClock.getTime()
            trial['trial_timestamp'] = time_trial - time_flip_img
            
        

            # checking for mouse clicks on stimuli DOES NOT WORK CURRENTLY
            #buttons = mouse.getPressed()
            if mouse.isPressedIn(button_click_left):
                #if (buttons == [1, 0, 0] and button_left.contains(mouse.getPos())):
                time_click = core.monotonicClock.getTime() 
                trial['response'] = 'left'
                trial['key_t']=time_click-exp_start
                trial['rt'] = time_click-time_flip_img
                break # break out of loop and go to next trial

            elif mouse.isPressedIn(button_click_right):
                #if (buttons == [1, 0, 0] and button_right.contains(mouse.getPos())):
                time_click = core.monotonicClock.getTime() 
                trial['response'] = 'right'  
                trial['key_t']=time_click - exp_start
                trial['rt'] = time_click - time_flip_img
                break # break out of loop and go to next trial

            # Save data in each frame to record mouse movement
            writer.writerow(trial)


        # Display fixation cross
        for frame in range(30): # Pause after each trial with fixation cross
            stim_fix.draw()
            win.flip()
                   

        #check if responses are correct
        if trial['response']=='right':
            trial['accuracy'] = 1 if trial['correct_resp']=='right' else 0
        elif trial['response']=='left':
            trial['accuracy'] = 1 if trial['correct_resp']=='left' else  0

        key = event.getKeys(keyList=('escape','q'))
        if key in KEYS_QUIT:
            win.close()
            core.quit()

        # Save response, accuracy, rt for each trial
        writer2.writerow(trial)
            
        
    
'''
DISPLAY INTRO TEXT AND AWAIT SCANNER TRIGGER
'''

# Define text objects
welcome_text= "Welcome to this experiment!\n\n\
The data collected will be used for a Cognitive Science exam project.\n\n\
Your data will be anonymised.\n\n\
By continuing you consent to your data being used for this purpose. It will not be used for other purposes.\n\n\
\n\n\
Press any key to continue."

instructions_text="Your task is to click on the specified \n\n\
item as fast as possible using the computer mouse provided. \n\n\
The mouse cursor will return to the same starting point after every trial. \n\n\
\n\n\
EXAMPLE: \n\n\
A specified item could be ZEBRA. \n\n\
Then your task is to click on the Zebra with the computer mouse. \n\n\
Press any key to continue."


practice_text= "First, you will complete six practice trials.\n\n\
If you have any questions please ask the experimenter.\n\n\
\n\n\
Press any key to start."

experimental_text = "Now the experiment will start.\n\n\
Again, your task is to click on the specified item as fast as possible.\n\n\
\n\n\
Press any key to begin!"

goodbye_text="The experiment is now done.\n\n\
Thank you for participating!\n\n\
\n\n\
Press any key to exit."

#Function for showing welcome/goodbye text and waiting for key press
def msg(txt):
    message = visual.TextStim(win, text = txt, height = 0.5)
    message.draw()
    win.flip()
    core.wait(1.5)
    event.waitKeys()

#Show instructions
msg(welcome_text)
msg(instructions_text)
msg(practice_text)

#event.waitKeys(keyList=KEYS_trigger)
exp_start=core.monotonicClock.getTime()

'''
CALL FUNCTION RUNNING THE EXPERIMENTAL LOOP
'''
for frame in range(1*FRAME_RATE):
     stim_fix.draw()
     win.flip()
# PRACTISE LOOP
practise_list = make_trial_list(trial_df = practisedf)
run_experiment(practise_list, exp_start)

msg(experimental_text)

# EXPERIMENTAL LOOP
# experimental_list = make_trial_list(trial_df = experimentaldf)
# run_experiment(experimental_list, exp_start)

csvfile.close()
csvfile2.close()

msg(goodbye_text)

'''
CREATING ONE MERGED DATAFRAME AND DOING CALCULATIONS
'''
columns_from_mouse_df = ['trial_number', 'phase', 'ID', 'age', 'gender', 'word', 'category','right_img', 'left_img', 'condition_trigger','img_trigger','trial_type', 'ypos', 'xpos', 'phase', 'trial_timestamp']
columns_from_accuracy_df = ['trial_number', 'phase', 'onset_word', 'onset_img', 'correct_resp', 'rt', 'response', 'accuracy', 'condition_trigger_t', 'key_t']

mouse_df = pd.read_csv(filename, usecols = columns_from_mouse_df)
accuracy_df = pd.read_csv(filename2, usecols = columns_from_accuracy_df)

df = mouse_df.merge(accuracy_df, on = ['trial_number', 'phase'], how = 'left')
filename3 = SAVE_FOLDER + 'merged/' + str(V['ID']) + str(utc_time) + '.csv'
df.to_csv(filename3)

