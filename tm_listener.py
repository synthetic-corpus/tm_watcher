'''
Purpose of this program is to help self test if tm_watcher transmits
information correctly
'''

import socket
import SocketServer
import pickle

# This Dictionary is contiously updated. Will eventually be initalized via file.

TMdatabase = {}

def updateDatabase(clientmessage):
    serial = clientmessage.keys()[0]
    client_dictionary = clientmessage[serial]
    databaseKeys = TMdatabase.keys()
    if serial in databaseKeys:
        TMdatabase[serial] = client_dictionary
    else:
        TMdatabase.update(clientmessage)
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
            print clientmessage
            updateDatabase(clientmessage)
            newSocket.send(echo_back)
        newSocket.close()
        print "Closed Connection From ",address
finally:
    sock.close()
