# testing to see if I can pull the serial number like I pull everything else.

import os
import datetime
import subprocess
from subprocess import PIPE
'''
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

print getSerial()

'''

def getCompName():
    #Returns an immutable tuple. Second thing in tuple is what I need as a string.
    rawout = subprocess.Popen(["scutil","--get","ComputerName"], stdout=PIPE, stderr=PIPE)
    #String_out is what you would get if you enter 'tmutil latestbackup' in terminal. Is a string.
    result = rawout.communicate()[0]
    # Easiest one so far
    return result

print getCompName()
