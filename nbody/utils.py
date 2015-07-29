import os, sys, inspect

def addToPath():    
    cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
    if cmd_folder not in sys.path:
        sys.path.insert(0, cmd_folder)
        
def addSubfolderToPath(subfolder):
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],subfolder)))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
        
def getScaledElapsedTime(time):
    #Prepare scaled elapsed time display
    #TODO: remove magic numbers

    displayUnit = "secs"
    displayTime = time
    if time > 600.0:
        displayTime = time / 60
        displayUnit = "mins"
        if time > 14400.0:
            displayTime = time / 3600
            displayUnit = "hours"
            if time > 172800.0:
                displayTime = time / 86400
                displayUnit = "days"
                if time > 10209600.0:
                    displayTime = time / 604800
                    displayUnit = "weeks"
                    if time > 31536000.0:
                        displayTime = time / 31536000
                        displayUnit = "years"
    return str(displayTime) + " " + displayUnit