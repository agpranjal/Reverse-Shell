import socket

SERVER_IP = ""  # will run on local machine
SERVER_PORT = 1234

s = socket.socket()
s.bind((SERVER_IP, SERVER_PORT))
s.listen(2)

while True:
    print("\nThe server is ready to accept new connections")
    temp_s, client_address = s.accept()
    print("Connection accepted from", client_address)

    while True:
        data = temp_s.recv(1000000)
        if data == b"exit":
            print("Connection closed")
            break

        output_string = data.decode()
        
        print(output_string, end="")
        while True:
            command = input().encode()
            
            if command != b"":
                break
            else:
                print(output_string.split("\n")[-1], end="")
        
        temp_s.send(command)
