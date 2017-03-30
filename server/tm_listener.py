'''
This program will listen to the input from  clients,
log entries, store data in files, and format for use by jQuery.

Program also updates .txt log files as its recieves data.

Path for files must be 'logs/simple' and 'logs/complex' relative to where This
script is located.
'''

import socket
import SocketServer
import pickle
import os.path
import json

# This Dictionary is contiously updated. Will eventually be initalized via file.
if os.path.exists("python-dictionary/tm-database.txt"):
    print "Data loaded from /python-dictionary/ folder\n***"
else:
    print "Data not present. Writing initial empty dictionary File.\n***"
    intializedFile = open("python-dictionary/tm-database.txt","w+")
    intializedFile.write("{}")
    intializedFile.close()
TMdatabase = eval(open("python-dictionary/tm-database.txt").read())
print "Database current is: "
print TMdatabase

# Update the tm-database.txt file
# @param is the TMdatabase python object.
def writeDatabase(TMdatabase):
    dump = json.dumps(TMdatabase)
    getfile = open("python-dictionary/tm-database.txt","w+")
    getfile.write(dump)
    getfile.close()

# Updates the Json object, to be interpreted by Javascript.
# Javascipt data strucure will be:
# [ {dict of name, serial, status, and time stamp}, {dict of name, serial, status, and time stamp} ]
# @Param TMdatabase python object
def writeJson(TMdatabase):
    json_object =[]
    for entry in TMdatabase:
        json_object.append(TMdatabase[entry])
    dump = json.dumps(json_object)
    json_file = open("website/js/table/json-table.js","w+")
    formatted_javascript = "var statusArray = " + dump + ";"
    json_file.write(formatted_javascript)
    json_file.close()

# Returns an actual log entry to append to log files.
# Reports data receieved only.
# @param the message from the network.
def logentrysimple(client_dictionary):
    dump = json.dumps(TMdatabase)
    template = " - Computer: #name# - Serial: #serial# - status: #status# \n"
    formatted_data = template.replace("#name#",client_dictionary["name"]).replace("#serial#",client_dictionary["serial"]).replace("#status#",client_dictionary["status"])
    output = "-->" + client_dictionary["timestring"] + formatted_data
    return output

# Returns an actual log entry to append to log files.
# Reports data receieved and resulting changes to tm-database.txt
# @param the message from the network.
def logentrycomplex(client_dictionary):
    dump = json.dumps(TMdatabase)
    template = " - Computer: #name# - Serial: #serial# - status: #status# \n"
    formatted_data = template.replace("#name#",client_dictionary["name"]).replace("#serial#",client_dictionary["serial"]).replace("#status#",client_dictionary["status"])
    output = "-->" + client_dictionary["timestring"] + formatted_data + "--> Current Database is: \n" + dump + '\n\n'
    return output

# Writes log entries to .txt
# @Param is dictionary from the client.
def logupdate(client_dictionary):
    # Gets a date string in the form of YYYY-MM-DD
    # Used to name the .txt files in the log
    today = client_dictionary["timestring"][0:10]
    logfilename_simple = "logs/simple/" + today + "-simple.txt"
    logfilename_complex = "logs/complex/" + today + "-complex.txt"
    logtext_simple = logentrysimple(client_dictionary)
    logtext_complex = logentrycomplex(client_dictionary)
    log=open(logfilename_simple,"a+")
    log.write(logtext_simple)
    log.close()
    log=open(logfilename_complex,"a+")
    log.write(logtext_complex)
    log.close()
    print "*** wrote to log \n***"

# Updates TMdatabase
# @Param is dictionary from the client.
# clientmessage is a dictionary formatted as
# {serial number:{rest of the update data}}
def updateDatabase(clientmessage):
    serial = clientmessage.keys()[0]
    client_dictionary = clientmessage[serial]
    databaseKeys = TMdatabase.keys()
    if serial in databaseKeys:
        TMdatabase[serial] = client_dictionary
    else:
        TMdatabase.update(clientmessage)
    logupdate(client_dictionary)
    writeDatabase(TMdatabase)
    # Updates Json database object
    writeJson(TMdatabase)

'''
Section below listens for incoming data.
Does things with the data via a function.
'''
# Make a sock?
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This line restarts the server when it terminates faster than usual.
# Honestly unsure why the books tells me I need this line.
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

known_port = 8881
sock.bind(('', known_port))

# Max number of clients waiting for connecting is 5
sock.listen(5)

# Loop, wait for connections.
print "Listening for connections..."
try:
    while 1:
        newSocket, address = sock.accept()
        print "Have connection from: ", address
        # Seems like these loops could be 'while true'?
        while 1:
            receivedData = newSocket.recv(1024)
            if not receivedData:
                break
            clientmessage = pickle.loads(receivedData)
            echo_back = "Have Signal. Updating with "
            print echo_back,clientmessage
            print "****"
            updateDatabase(clientmessage)
            newSocket.send(echo_back)
        newSocket.close()
        print "Closed Connection From ",address
finally:
    sock.close()
