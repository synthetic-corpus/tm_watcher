import os
import datetime
import time

aTime = datetime.datetime(2017,03,10,9,45)
currentTime = datetime.datetime.now()
deltaTime = currentTime - aTime
print "arbitaray time ",aTime
print "current is ,",currentTime
print "elasped is ",deltaTime

twohours = datetime.timedelta(hours = 2)
print "Length of time ",twohours

if deltaTime > twohours:
    print "More than Two hours"
else:
    print "Not more than two hours"
