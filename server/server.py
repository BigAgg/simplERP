import socket
import threading
import time

HOST = "10.1.4.86"
PORT = 5050
FORMAT = "utf-8"
MAXPLAYERS = 4


def connection(conn, addr):
    try:
        with conn:
            if len(threading.enumerate()) - 1 > MAXPLAYERS:
                conn.sendall("The Server is full".encode(FORMAT))
                return
            print(f"[NEW CONNECTION] Connected to {addr}")
            conn.sendall("Connected".encode(FORMAT))
            data = None
            while data != "!DISCONNECT":
                data = conn.recv(1024).decode(FORMAT)
                if not data:
                    break
                print(data)
                if data == "!DISCONNECT":
                    break
                conn.sendall(data.encode(FORMAT))
            conn.sendall("Disconnected".encode(FORMAT))
            print(f"Disconnected {addr}")
    except ConnectionResetError:
        print(f"{addr} lost connection")


def main():
    print("[STARTING] Server is starting...")
    while 1:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            if len(threading.enumerate()) - 1 <= MAXPLAYERS:
                s.listen()
                print("[LISTENING] Server is listening...")
                conn, addr = s.accept()
                client = threading.Thread(target=connection, args=(conn, addr,))
                client.start()
                for thread in threading.enumerate():
                    print(thread.name)
            else:
                print("[SERVER MSG] Server is full")
                while len(threading.enumerate()) - 1 >= MAXPLAYERS:
                    time.sleep(2)


if __name__ == "__main__":
    main()
