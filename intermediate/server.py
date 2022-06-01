import socket

# AF_INET states that wew want an internet socket rather ahn a UNIX socket
# SOCK_STREAM is for the protocol that we choose, TCP. For UDP it will be SOCK_DGRAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create a server
s.bind(("127.0.0.1", 9999))
s.listen()
print("Listening...")

while True:
    client, address = s.accept()
    print("Connected to {}".format(address))
    message = "Hello Client!"
    client.send(message.encode('ascii'))
    client.close()
