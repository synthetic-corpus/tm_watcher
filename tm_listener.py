'''
Purpose of this program is to help self test if tm_watcher transmits
information correctly
'''

import socket
import SocketServer
import pickle
import os.path

# This Dictionary is contiously updated. Will eventually be initalized via file.
if os.path.exists("python-dictionary/tm-database.txt"):
    print "Data loaded from /python-dictionary/ folder\n***"
else:
    print "Data not present. Writing initial empty dictionary File.\n***"
    intializedFile = open("python-dictionary/tm-database.txt","w+")
    intializedFile.write("{}")
    intializedFile.close()
TMdatabase = eval(open("python-dictionary/tm-database.txt").read())
print TMdatabase

# Returns an actual log entry to append to log files.
# @param the message from the network.
def logentry(client_dictionary):
    template = " - Computer: #name# - Serial: #serial# - status: #status# \n"
    formatted_data = template.replace("#name#",client_dictionary["name"]).replace("#serial#",client_dictionary["serial"]).replace("#status#",client_dictionary["status"])
    output = client_dictionary["timestring"] + formatted_data
    return output

# Writes log entries to .txt
# @Param is dictionary from the client.
def logupdate(client_dictionary):
    key = clientmessage.keys()[0]
    # Gets a date string in the form of YYYY-MM-DD
    # Used to name the .txt files in the log
    today = client_dictionary["timestring"][0:10]
    logfilename = "logs/" + today + ".txt"
    logtext = logentry(client_dictionary)
    log=open(logfilename,"a+")
    log.write(logtext)
    log.close()
    print "*** wrote to log \n ***"

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
# Print Statments for debugging.
    print "Databse looks like: "
    print TMdatabase

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
