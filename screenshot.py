#!/usr/bin/env python3
'''
Plan:
1. In desktop, find files that have the 'screenshot' pattern
2. Redirect that file to screenshots folder
3. Rename the screenshot
'''

import os
from os import path
import shutil
from datetime import date
import glob


def cwd_to_desktop():
    '''
    change cwd to desktop where screenshots go to by default and find files
    '''

    os.chdir('/Users/therekromo/Desktop') # change cwd to desktop bc this is where screenshots go to by default

    sc_list = []
    for file in glob.glob('*Screen Shot*'): #find files that have 'Screen Shot' in them and add their dir path to list
        file_path = os.getcwd() + '/' + file
        sc_list.append(file_path)
    if not sc_list:
        print('No Screenshots found on desktop. All good!')
    move_screenshots(sc_list)


def move_screenshots(sc_list): #move screenshots to screenshot folder and rename them with todays date
    curr_at = 0
    for file_path in sc_list:
        today = str(date.today())

        while path.exists(path_to := r'/Users/therekromo/Desktop/Screenshots'+ '/' + today + f"({curr_at+1})" + ".png"):
            curr_at += 1
        shutil.move(file_path, path_to)
        print(file_path)
    print('All screenshots moved successfully! Check your Screenshots folder on your desktop!')


cwd_to_desktop()