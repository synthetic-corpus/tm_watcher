#!/usr/bin/env python
# this will be where I make the TM monitor.
# Program is designed to run at start up, in background, no interaction or alerts from user.


# Import Relevant modules to access Mac OS.
import os
import datetime
import subprocess
from subprocess import PIPE
import socket
import pickle
import time

# Used to get the computer's Serial number
def getSerial():
    #Returns an immutable tuple. Second thing in tuple is what I need as a string.
    rawout = subprocess.Popen(["system_profiler","SPHardwareDataType"], stdout=PIPE, stderr=PIPE)
    #String_out is what you would get if you enter 'tmutil latestbackup' in terminal. Is a string.
    result = rawout.communicate()[0]
    start_cut = result.find("Serial Number")
    # 24 is the Lengthe betwen "Serial Number" and where the Serial number starts
    # 13 accounts for the lenght of serial number itself.
    string_out = result[start_cut + 24:start_cut +24 +12]
    return string_out

# Gets the Computer name
def getCompName():
    #Returns an immutable tuple. Second thing in tuple is what I need as a string.
    rawout = subprocess.Popen(["scutil","--get","ComputerName"], stdout=PIPE, stderr=PIPE)
    result = rawout.communicate()[0]
    # Easiest one so far
    string_out = result[:-1] # Done to remove a non-character line break.
    return string_out

# String to Time Stamp
# Takes terminal output like '/Volumes/140027/Backups.backupdb/Joel's Imac/2017-03-10-124532'
# Converts it into a python datetime object.
def terminalToDatetime(string):
    # two lines below converts:
    # string = "/Volumes/140027/Backups.backupdb/Joel's Imac/2017-03-10-124532"
    # rawdate = "2017-03-10-124532"
    index = string.rfind("/")
    rawdate = string[index + 1:]
    # Lines below converts "2017-03-10-124532"
    # Into ['2017','03','10','12','45'] Year, Month, day etc...
    timeList = rawdate.split("-")
    hours = timeList[3][0:2]
    minutes = timeList[3][2:4]
    timeList[3] = hours
    timeList.append(minutes)
    # Loop Below converts list of strings to list of integers
    timeInt =[]
    for string in timeList:
        timeInt.append(int(string))
    # Takes input from list and converts to a date.
    convertedDate = datetime.datetime(timeInt[0],timeInt[1],timeInt[2],timeInt[3],timeInt[4])
    return convertedDate

# Reads the string output from getBackupString()
def readBackUpOutput(string):
    #Checks for the errror message using string.find
    if string.find("Unable to locate machin") != -1:
        return "disconnected"
    elif string.find("error in the re") != -1:
        return 'problem'
    else:
        # Compares time. Ensures not longer than 90 minutes.
        last_good_backup = terminalToDatetime(string)
        current_time = datetime.datetime.now()
        gap = current_time - last_good_backup
        ninety_minutes = datetime.timedelta(hours = 1, minutes =30)
        if gap < ninety_minutes:
            return "working"
        else:
            return "overdue"

# Runs a 'tmutil latestbackup' as a termainal command.
# Returns result as a string.
# the Command 'tmutil latestbackup' returns either the file path to latest backup...
# Or "unable to locate machine..." if back up is disconnected.
def getBackupString():
    # Line below immutable tuple. Second thing in tuple is what I need as a string.
    rawout = subprocess.Popen(["tmutil","latestbackup"], stdout=PIPE, stderr=PIPE)
    # String_out is what you would get if you enter 'tmutil latestbackup' in terminal. Is a string.
    result = rawout.communicate()
    # If then statements may not be needed, but kept just in case anything goes wrong.
    if len(result[0]) > 0:
        string_out = result[0]
    elif len(result[1]) > 0:
        string_out = result[1]
    else:
        string_out = "error in the read string"
    return string_out

# Function sends data overnetwork.
def sendThis(json_out):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('127.0.0.1',443))
        sock.send(json_out)
        response_data = sock.recv(1024)
        sock.close()
    except:
        None
        # Do nothing. Program is meant to run background,
        # no input or alerts to user needed.

# Triggers all other functions
# Returns output as print for now.
# Sends data to the script on the server.
def networkOutput():
    terminal_output = getBackupString()
    machine_status = readBackUpOutput(terminal_output)
    machine_serial = getSerial() #Use mac OS module to get machine serial
    machine_name = getCompName() #Get Mac OS module to get machine name
    machine_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') #Returns timestamp as string.
    python_dictionary = {machine_serial:{"status":machine_status,"serial":machine_serial,"name":machine_name,"timestring":machine_timestamp}}
    python_out = pickle.dumps(python_dictionary)
    sendThis(python_out)

# Loops the networkoutput function.
# Sends data every five minutes.
# Final version will send every fifteen.

def checkupLoop():
    while True:
        networkOutput()
        time.sleep(300)

checkupLoop()
