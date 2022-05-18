import numpy as np
import pandas as pd

def add_trigger(df:pd.DataFrame, trigger:int, array, first_img_display, sr_eeg, st_first_image, columnname:str, image_onset = 'onset_image'):
    '''
    returns an array of events with new events added.

    args:
        df(pd.Dataframe): A dataframe containing time points from mouse tracking.
        trigger(int): The wanted event code
        array: Array of events
        first_img_display: Timing for display of first images in mousetracking (measured in seconds)
        sr_eeg: The sampling rate of EEG data
        sample_time_first_image: The EEG sample for displaying the first images
        columnname: The name of the column containing time stamps you want to add events for


    '''
    df[columnname] = (df[image_onset] - first_img_display + df[columnname]) * sr_eeg + st_first_image

    # making it into integer since samples can only be whole numbers
    df[columnname] = df[columnname].astype(int)

    for i in range(len(df)): 
        new_array = [[df[columnname][i], 0, trigger]]
        array = np.append(array, new_array, axis = 0)
    
    return array

def average_power_time(power, channel_indices, freq_indices_b, freq_indices_a, time_indicies_b, time_indicies_a):
    '''
    returns the averaged power over channels and frequencies for each time point. 

    args:
        power: 
        channel_indices: the channels wanted
        freq_indices_b: the lowest frequency index wanted
        freq_indices_e: the highest frequency index wanted
        time_indices_b: the lowest time index wanted
        time_indices_e: the highest time index wanted
    '''
    ## getting the channels wanted and the wanted frequencies
    data = power.data[np.array(channel_indices), freq_indices_b:freq_indices_a, time_indicies_b:time_indicies_a]

    ## averaging over the channels
    average = np.mean(data, axis = 0)

    ## averaging over frequencies
    average = np.mean(average, axis = 0)
 
    return average