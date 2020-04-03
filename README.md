# ReverseShell
A demonstration of reverse shell in python3

### What is a Reverse Shell ?

Also known as shell shoveling, Reverse Shell redirects the output and input of a shell to a service so as to enable remote access to that shell.

### Requirements:
+ python3
+ subprocess

### Install subprocess:
`pip3 install subprocess`

### Configuration

Before execution, enter the server ip address in client.py
> SERVER_IP = "your_server_ip_address_goes_here"

By default, the server and client would both run on the same machine unless the SERVER_IP is specified.

### How to run ?
On the server machine, run `python3 server.py`

On the client machine, run `python3 client.py`

The client machine's shell will now be available from the server machine.
