import psutil

def batterystat(s):
    if psutil.sensors_battery().percent >= 85:
        return "Victim Fully Charged!"
    
    return ""



def batterystatus():
  p = psutil.sensors_battery().percent
  print(f"{p}% Battery Status {batterystat(p)}")

batterystatus()
