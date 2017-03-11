# this will be where I make the TM monitor.


# Import Relevant modules to access Mac OS.
import os
import datetime
import subprocess
from subprocess import PIPE

#Used to get the computer's Serial number
def getSerial():
    #Returns an immutable tuple. Second thing in tuple is what I need as a string.
    rawout = subprocess.Popen(["system_profiler","SPHardwareDataType"], stdout=PIPE, stderr=PIPE)
    #String_out is what you would get if you enter 'tmutil latestbackup' in terminal. Is a string.
    result = rawout.communicate()[0]
    start_cut = result.find("Serial Number")
    # 24 is the Lengthe betwen "Serial Number" and where the Serial number starts
    # 13 accounts for the lenght of serial number itself.
    string_out = result[start_cut + 24:start_cut +24 +13]
    return string_out

def getCompName():
    #Returns an immutable tuple. Second thing in tuple is what I need as a string.
    rawout = subprocess.Popen(["scutil","--get","ComputerName"], stdout=PIPE, stderr=PIPE)
    #String_out is what you would get if you enter 'tmutil latestbackup' in terminal. Is a string.
    result = rawout.communicate()[0]
    # Easiest one so far
    return result

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
        return "disconnected"
    else:
        #Compares time. Ensures not longer than 90 minutes.
        last_good_backup = terminalToDatetime(string)
        current_time = datetime.datetime.now()
        gap = current_time - last_good_backup
        ninety_minutes = datetime.timedelta(hours = 1, minutes =30)
        if gap < ninety_minutes:
            return "working"
        else:
            return "overdue"

def getBackupString():
    #Returns an immutable tuple. Second thing in tuple is what I need as a string.
    rawout = subprocess.Popen(["tmutil","latestbackup"], stdout=PIPE, stderr=PIPE)
    #String_out is what you would get if you enter 'tmutil latestbackup' in terminal. Is a string.
    result = rawout.communicate()
    if len(result[0]) > 0:
        string_out = result[0]
    elif len(result[1]) > 0:
        string_out = result[1]
    else:
        string_out = "error in the read string"
    return string_out

def networkOutput():
    terminal_output = getBackupString()
    #print terminal_output
    machine_serial = getSerial() #Use mac OS module to get machine serial
    machine_name = getCompName() #Get Mac OS module to get machine name
    if readBackUpOutput(terminal_output) == "disconnected":
        #Send network 'red signal with machine info.
        print "Back up for ",machine_name," is offline."
    elif readBackUpOutput(terminal_output) == "overdue":
        #Send network 'yellow signal' with machine info.
        print "Back up for ",machine_name," is overdue."
    elif readBackUpOutput(terminal_output) == "working":
        #Send network Green signal with machine info
        print "Back up for ",machine_name," is working."
    else:
        print "something is wrong with the code. What went wrong?"

networkOutput()
