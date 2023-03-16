# servidor do socket

import socket

s = socket.socket()                         # Create a socket object
host = socket.gethostname()                 # Get local machine name
port = 1234                                # Reserve a port for your service.
s.bind((host, port))                        # Bind to the port

s.listen(5)

while True:
    
    c, addr = s.accept()                # Establish connection with client.
    try:
        print('Conexão estabelecida com: ', addr)
        data = c.recv(1024)
        while (data.decode != 'SAIR'):
            if (data.decode == 'SAIR'):
                c.close()
                break
            else:
                print("> CLIENTE: "+data.decode())
                c.send(input().encode())
    except:
        print('erro')
        c.close
        break

