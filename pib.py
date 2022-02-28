import os
import win32api
import psutil


print("Productivity Is Best")
print("Enter blackist file:")
file = input("Full Path: ")
with open(file) as fl:
    progs = fl.read().split("|")

print("Opening...")

def send_message(string):
    win32api.MessageBox(0, "Unproductive App Killed. (" + string + ")", "PIB")

def taskkill(appname):
    os.system("taskkill /F /IM " + appname)


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;




YESNO = input("WARNING: This will kill any apps and any unsaved work will be lost!\nPress Enter to conitiue")
print("Running")
while True:
    for app in progs:
        if checkIfProcessRunning(app):        
            taskkill(app)
            send_message(app)

        else:
            pass
