import socket
from time import perf_counter

HOST = "10.1.4.86"
PORT = 5050
FORMAT = "utf-8"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024).decode(FORMAT)
    if data == "Connected" and data != "The Server is full":
        print(data)
        while (inp := input()) != "!DISCONNECT":
            s.sendall(inp.encode(FORMAT))
            start_time = perf_counter()
            data = s.recv(1024).decode(FORMAT)
            print(f"Recieved message in {perf_counter() - start_time}")
            print(data)
        s.sendall(inp.encode(FORMAT))
        data = s.recv(1024).decode(FORMAT)
        print(data)
    else:
        print(data)
    s.close()


