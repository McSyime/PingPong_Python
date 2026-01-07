import socket

HOST = "127.0.0.1"
PORT = 5005  # Hub-Port

ROUTE = [
    ("Pang1", "127.0.0.1", 5000),
    ("Pong1", "127.0.0.1", 5001),
    ("Pang2", "127.0.0.1", 5002),
    ("Pong2", "127.0.0.1", 5003),
]

def call_node(host, port, value):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(str(value).encode("utf-8"))
        data = s.recv(1024)
    return int(data.decode("utf-8").strip())

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as hub:
        hub.bind((HOST, PORT))
        hub.listen()
        print(f"Hub listening on {HOST}:{PORT}")

        while True:
            conn, addr = hub.accept()
            with conn:
                data = conn.recv(1024)
                value = int(data.decode("utf-8").strip())
                print(f"[Hub] Start: {value}")

                for name, h, p in ROUTE:
                    old = value
                    value = call_node(h, p, value)
                    print(f"[Hub] {name}: {old} -> {value}")

                conn.sendall(str(value).encode("utf-8"))
                print(f"[Hub] Final result sent: {value}")

if __name__ == "__main__":
    main()
