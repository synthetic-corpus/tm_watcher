'''
Purpose of this program is to help self test if tm_watcher transmits
information correctly
'''

import socket
import SocketServer

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
            echo_back = "We have this: " + receivedData
            print echo_back
            newSocket.send(echo_back)
        newSocket.close()
        print "Closed Connection From ",address
finally:
    sock.close()
