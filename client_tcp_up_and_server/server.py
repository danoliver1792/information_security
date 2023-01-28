import socket

connection_object = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket created successfully")

host = "localhost"
port = 5432

# connection between client and server via host and port
connection_object.bind((host, port))
message = "\nServer: hello client"

# as long as it's true (1)
while 1:
    data, address = connection_object.recvfrom(4096)

    if data:
        connection_object.sendto(data + (message.encode()), address)
