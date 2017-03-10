# this will be where I make the TM monitor.


# Import Relevant modules to access Mac OS.
import os
import subprocess
from subprocess import PIPE
#Write a function that (Check) checks the last time Machine back.
# Takes no Paramters. Returns the time of the last back up as a Date.
rawout = subprocess.Popen(["tmutil","latestbackup"], stdout=PIPE, stderr=PIPE)
string = rawout.communicate()[1]
print string[2:]
'''def check_last_backup():
    #time_stamp = subprocess.check_output("ls -l")
    print subprocess.check_output("tmutil latestbackup")

check_last_backup()'''
#write another function. (Compare) Takes in a a date. Compares it to current System time.
# Returns 'on time' 'late' 'very late' 'error'

#Fucntion that runs on a infinute loop.
#Runs Compare every two hours.
#Prints out results.
#If Very late, makes a system beep.
