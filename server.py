import socket

HOST = '127.0.0.1'
PORT = 8081

server = socket.socket()
server.bind((HOST, PORT))

print('--- Server Started ---')
print('Server listening for client connection...')
server.listen(1)
# Above, this allows the server to accept connections
# 1 means the number of connections the server can queue before rejecting them

client, client_address = server.accept()
# Above, this is what explicitly accepts the connections
# 'client' is the socket object that we will use to send commands, etc. This socket is how the server communicates
# 'client_adddress' is a tuple of IP and Port
print(f'{client_address} connected to the server')

while True:
    command = input("Enter command: ")
    command = command.encode()
    client.send(command)
    print('[+] Command sent')
    output = client.recv(1024)
    output = output.decode()
    print(output)