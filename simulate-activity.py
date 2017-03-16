'''
This program runs a simulation.
Sends several network packages to ensure they are processed correctly.
'''


# Import Relevant modules to access Mac OS.
import os
import datetime
import subprocess
from subprocess import PIPE
import socket
import pickle
import time

# An Array of simulated output from this program.

simulationArray = [
{'C02JP0B4DKQ2':{'status':'working','serial':'C02JP0B4DKQ2','name':"Joel's macbook",'timestring':'2017-03-01 10:00:00'}},
{'BATMAN--DKQ2':{'status':'disconnected','serial':'BATMAN--DKQ2','name':"Batmans's macbook",'timestring':'2017-03-01 10:00:03'}},
{'JOKER---DKQ2':{'status':'disconnected','serial':'JOKER---DKQ2','name':"Funny guy's macbook",'timestring':'2017-03-01 10:00:06'}},
{'C02JP0B4DKQ2':{'status':'working','serial':'C02JP0B4DKQ2','name':"Joel's macbook",'timestring':'2017-03-01 10:00:09'}},
{'WOLVERINE-Q2':{'status':'overdue','serial':'WOLVERINE-Q2','name':"Feral Canadian's iMac",'timestring':'2017-03-01 10:00:12'}},
{'JOKER---DKQ2':{'status':'overdue','serial':'JOKER---DKQ2','name':"Funny guy's macbook",'timestring':'2017-03-01 10:00:15'}},
{'BATMAN--DKQ2':{'status':'working','serial':'BATMAN--DKQ2','name':"Batmans's macbook",'timestring':'2017-03-01 10:00:18'}},
{'WOLVERINE-Q2':{'status':'working','serial':'WOLVERINE-Q2','name':"Feral Canadian's iMac",'timestring':'2017-03-01 10:00:21'}},
{'JOKER---DKQ2':{'status':'overdue','serial':'JOKER---DKQ2','name':"Funny guy's macbook",'timestring':'2017-03-01 10:00:24'}}
]

# Function sends data overnetwork.
def sendThis(json_out):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1',8881))
    sock.send(json_out)
    response_data = sock.recv(1024)
    sock.close()

# Takes in Simulated packets. Sends them out exactly as it would if it was real dictionary.
# Structure of simulation Data:
# {machine_serial:{"status":machine_status,"serial":machine_serial,"name":machine_name,"timestring":machine_timestamp}}
def networkOutput(simulationData):
    python_dictionary = simulationData
    python_out = pickle.dumps(python_dictionary)
    sendThis(python_out)

def simulate():
    sentCount = 0
    for message in simulationArray:
        networkOutput(message)
        time.sleep(3)
        sentCount = sentCount + 1
        print "--> sent a message...",sentCount
    print "--> All Messages sent"

simulate()
