import socket

connection_object = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("socket client successfully created")

host = "localhost"
port = 5433
port_server = 5432

message = "Hello server"

try:
    print(f"Client: {message}")
    connection_object.sendto(message.encode(), (host, port_server))

    # Expecting a connection of 4096 bytes
    data, server = connection_object.recvfrom(4096)
    data = data.decode()
    print(f"Client: {data}")
finally:
    print("Client: closing the connection")
    connection_object.close()
