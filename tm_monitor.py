# this will be where I make the TM monitor.


# Import Relevant modules to access Mac OS.
import os
import subprocess
from subprocess import PIPE
#Write a function that (Check) checks the last time Machine back.
# Takes no Paramters. Returns the time of the last back up as a Date.
def readBackUpStatus(string):
    #Checks for the errro message using string.find
    if string.find("Unable to locate machin") != -1:
        return "Back up not Configured"
    else:
        return "This is the last time it backed up"

def getBackupStatus():
    #Returns an immutable tuple. Second thing in tuple is what I need as a string.
    rawout = subprocess.Popen(["tmutil","latestbackup"], stdout=PIPE, stderr=PIPE)
    #String_out is what you would get if you enter 'tmutil latestbackup' in terminal. Is a string.
    string_out = rawout.communicate()[1]
    print string_out
    status = readBackUpStatus(string_out)
    return status

print getBackupStatus()

# Write a fucntion that takes a String as Parameter. Reads it. Returns "no Back up Present" or "Date of last back up"


#write another function. (Compare) Takes in a a date. Compares it to current System time.
# Returns 'on time' 'late' 'very late' 'error'

#Fucntion that runs on a infinute loop.
#Runs Compare every two hours.
#Prints out results.
#If Very late, makes a system beep.
