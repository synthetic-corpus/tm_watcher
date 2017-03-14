'''
Purpose of this program is to help self test if tm_watcher transmits
information correctly
'''

import socket
import SocketServer

# Make a sock?
sock = socket.socket(socket.AF_INET, socket.SOC_STREAM)

# This line restarts the server when it terminates faster than usual.
# Honestly unsure why the books tells me I need this line.
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

known_port = 8881
sock.bind(('', known_port))

# Max number of clients waiting for connecting is 5
sock.listen(5)

# Loop, wait for connections.

try:
    while 1:
        newSocket, address = sock.accept()
        print "Have connection from: ", address
        # Seems like these loops could be 'while true'?
        while 1:
            recievedData = newSocket.recv(1024)
            if not recievedData:
                break
            newSocket.send("recieved this: ",receivedData)
        newSocket.close()
        print "Closed Connection From ",address
finally:
    sock.close()
