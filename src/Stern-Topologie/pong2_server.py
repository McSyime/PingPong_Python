import socket

HOST = "127.0.0.1"
PORT = 5003

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Pong2 listening on port 5003")

        while True:
            conn, _ = s.accept()
            with conn:
                data = conn.recv(1024)
                n = int(data.decode("utf-8").strip())
                n += 1
                conn.sendall(str(n).encode("utf-8"))

if __name__ == "__main__":
    main()
