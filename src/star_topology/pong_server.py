import argparse
import socket

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 5001


def parse_args():
    parser = argparse.ArgumentParser(description="Pong1 Server")
    parser.add_argument(
        "--host",
        default=DEFAULT_HOST,
        help=f"Host to bind to (default: {DEFAULT_HOST})"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=DEFAULT_PORT,
        help=f"Port to listen on (default: {DEFAULT_PORT})"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    host = args.host
    port = args.port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Pong1 listening on {host}:{port}")

        while True:
            conn, _ = s.accept()
            with conn:
                data = conn.recv(1024)
                n = int(data.decode("utf-8").strip())
                n += 1
                conn.sendall(str(n).encode("utf-8"))


if __name__ == "__main__":
    main()
