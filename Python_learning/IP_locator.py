import socket
if __name__ == "main":
    hostname = "www.harvoxx.com"
    address = socket.gethostbyname(hostname)
    print(f"The IP Address for {hostname} is {address}")