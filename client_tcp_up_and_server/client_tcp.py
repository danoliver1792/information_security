import socket
import sys


def main():
    """ testing TCP/IP connection """
    try:
        connection_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print("connection failed")
        print(f"Error: {error}")
        sys.exit()

    print("socket created successfully")

    # defining which host will be connected
    host_connect = input("Enter host or IP to connect: ")
    port = input("Enter port to connect: ")

    # connecting and closing
    try:
        connection_object.connect((host_connect, int(port)))
        print(f"TCP client successfully connected: {host_connect} to the port {port}")
        connection_object.shutdown(2)
    except socket.error as error:
        print("connection failed")
        print(f"Error: {error}")
        sys.exit()


# calling the function
if __name__ == "__main__":
    main()
