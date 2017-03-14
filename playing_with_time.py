import os
import datetime
import time

currentTime = datetime.datetime.now()
print "Time Variable is: ",currentTime
print "Datetime method returns:  ",datetime.datetime.now()
print "Now sleeping..."
counter = 0
while counter != 7:
    print "zzz.."
    time.sleep(5)
    counter = counter +1

print "Time Variable is: ",currentTime
print "Datetime method returns:  ",datetime.datetime.now()
