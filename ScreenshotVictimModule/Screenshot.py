import pyautogui
import os

class RATtackScreenshot:
    def init(self,screenshotname):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\')
        pyautogui.screenshot().save(desktop + str(screenshotname))

p1 = RATtackScreenshot("Markdd.jpg")
