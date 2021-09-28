#!/usr/bin/env python3
import os

def go_to_desktop():
    current_dir = os.getcwd()
    print(current_dir)

    new_dir = os.chdir('/../')
    print(new_dir)

go_to_desktop()