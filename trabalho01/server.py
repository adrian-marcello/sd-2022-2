# servidor do socket

import socket

s = socket.socket()                         # Create a socket object
host = socket.gethostname()                 # Get local machine name
port = 1234                                # Reserve a port for your service.
s.bind((host, port))                        # Bind to the port

s.listen(5)

while True:
    
    c, addr = s.accept()             # Establish connection with client.
    msg = ''
    try:
        print('Conexão estabelecida com: ', addr)
        

        while (msg != 'SAIR'):
            data = c.recv(1024)
            msg = data.decode()
            if (msg == 'SAIR'):
                c.close()
                break
            else:
                print("> CLIENTE: "+msg)
                c.send(input().encode())
    except:
        print('erro')
        c.close
        break

