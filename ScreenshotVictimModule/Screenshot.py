import pyautogui







class hack:
    def __init__(self,screenshotname):
        self.screenshotname = screenshotname

        self.screenshotname = pyautogui.screenshot()
        self.screenshotname.save(screenshotname)


    def func(self):
        s = self.screenshotname
        return s

p1 = hack("John.jpg")#Call this from another module so the name will be varied.)
p1.func()
