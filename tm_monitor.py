# this will be where I make the TM monitor.


# Import Relevant modules to access Mac OS.
import os
import datetime
import subprocess
from subprocess import PIPE

#String to Time Stamp
#Takes terminal output like '/Volumes/140027/Backups.backupdb/Joel's Imac/2017-03-10-124532'
#Converts it into a datetime object.
def terminalToDatetime(string):
    # two lines below convert:
    # string = "/Volumes/140027/Backups.backupdb/Joel's Imac/2017-03-10-124532"
    # rawdate = "2017-03-10-124532"
    index = string.rfind("/")
    rawdate = string[index + 1:]
    # Lines below conver "2017-03-10-124532"
    # Into ['2017','03','10','12',45] Year, Month, day etc...
    timeList = rawdate.split("-")
    hours = timeList[3][0:2]
    minutes = timeList[3][2:4]
    timeList[3] = hours
    timeList.append(minutes)
    #Loop Below converts list of strings to list of integers
    timeInt =[]
    for string in timeList:
        timeInt.append(int(string))
    #Takes input from list and converts to a date.
    convertedDate = datetime.datetime(timeInt[0],timeInt[1],timeInt[2],timeInt[3],timeInt[4])
    return convertedDate

#Write a function that (Check) checks the last time Machine back.
# Takes no Paramters. Returns the time of the last back up as a Date.
def readBackUpOutput(string):
    #Checks for the errro message using string.find
    if string.find("Unable to locate machin") != -1:
        return "Back up not Configured"
    else:
        #Runs a process to be written and eventually returns a time stamp variable.
        return "This is the last time it backed up"

def getBackupStatus():
    #Returns an immutable tuple. Second thing in tuple is what I need as a string.
    rawout = subprocess.Popen(["tmutil","latestbackup"], stdout=PIPE, stderr=PIPE)
    #String_out is what you would get if you enter 'tmutil latestbackup' in terminal. Is a string.
    string_out = rawout.communicate()[1]
    print string_out
    status = readBackUpOutput(string_out)
    return status

print getBackupStatus()

# Write a fucntion that takes a String as Parameter. Reads it. Returns "no Back up Present" or "Date of last back up"


#write another function. (Compare) Takes in a a date. Compares it to current System time.
# Returns 'on time' 'late' 'very late' 'error'

#Fucntion that runs on a infinute loop.
#Runs Compare every two hours.
#Prints out results.
#If Very late, makes a system beep.
