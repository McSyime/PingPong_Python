"""
Simple Ping client.
Connects to the Hub, sends an integer and prints the final response.
"""
import argparse
import socket

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 5005  # Hub-Port
NUMBER = 1

def parse_args():
    parser = argparse.ArgumentParser(description="TCP Ping Client")
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    return parser.parse_args()

def main():
    args = parse_args()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((args.host, args.port))
        print(f"Connected to Hub {args.host}:{args.port}")

        sock.sendall(str(NUMBER).encode("utf-8"))
        print(f"Sent: {NUMBER}")

        data = sock.recv(1024)
        print(f"Received: {data.decode('utf-8').strip()}")

if __name__ == "__main__":
    main()
