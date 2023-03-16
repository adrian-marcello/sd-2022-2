#cliente do socket

import socket                          # Import socket module

s = socket.socket()                    # Create a socket object
host = socket.gethostname()            # Get local machine name
port = 1234                           # Reserve a port for your service.

s.connect((host, port))
msg = ""
while (msg != "SAIR"):
    msg = input()
    s.send(msg.encode())
    if (msg != "SAIR"):
        data = s.recv(1024)
        print("> SERVIDOR: "+data.decode())
    else:
        break
s.close()                              # Close the socket when done