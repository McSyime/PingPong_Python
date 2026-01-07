#!/usr/bin/env python3
"""
Pang server.
Forwards data between Ping and Pong and increments the value.
"""

import argparse  # Provides argument parser
import socket  # Provides networking (socket) functionality

# Pang listens here (Ping connects here)
DEFAULT_PANG_HOST = "127.0.0.1"
DEFAULT_PANG_PORT = 5000

# Pong server address
DEFAULT_PONG_HOST = "127.0.0.1"
DEFAULT_PONG_PORT = 5001


def parse_args():
    parser = argparse.ArgumentParser(description="Pang Server")
    parser.add_argument(
        "--host",
        default=DEFAULT_PANG_HOST,
        help=f"Host to bind to (default: {DEFAULT_PANG_HOST})"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=DEFAULT_PANG_PORT,
        help=f"Port to listen on (default: {DEFAULT_PANG_PORT})"
    )
    parser.add_argument(
        "--pongHost",
        default=DEFAULT_PONG_HOST,
        help=f"Pong server host (default: {DEFAULT_PONG_HOST})"
    )
    parser.add_argument(
        "--pongPort",
        type=int,
        default=DEFAULT_PONG_PORT,
        help=f"Pong server port (default: {DEFAULT_PONG_PORT})"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    host = args.host
    port = args.port
    pong_host = args.pongHost
    pong_port = args.pongPort

    # Create a TCP socket (IPv4, stream-based)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as pang_socket:
        # Bind the socket to the given host and port
        pang_socket.bind((host, port))

        # Start listening for incoming connections
        pang_socket.listen()
        print(f"Pang server listening on {host}:{port}")

        # Server runs forever and handles one client at a time
        while True:
            # Wait for a client to connect
            ping_conn, ping_addr = pang_socket.accept()
            print(f"Connection from Ping {ping_addr}")

            # Use 'with' to automatically close the connection
            with ping_conn:
                # Receive up to 1024 bytes from the client
                data = ping_conn.recv(1024)

                # If no data was received, the client closed the connection
                if not data:
                    print("No data received")
                    continue

                # Convert bytes to string and remove whitespace
                message = data.decode("utf-8").strip()
                print(f"Received from Ping: {message}")

                # Increment spin
                number = int(message) + 1

                # Send to Pong
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as pong_conn:
                    pong_conn.connect((pong_host, pong_port))
                    pong_conn.sendall(str(number).encode("utf-8"))
                    print(f"Sent to Pong: {number}")

                    # Receive from Pong
                    pong_response = pong_conn.recv(1024)

                pong_value = int(pong_response.decode("utf-8").strip())
                print(f"Received from Pong: {pong_value}")

                # Increment again and send back to Ping
                pong_value += 1
                response = str(pong_value)

                ping_conn.sendall(response.encode("utf-8"))
                print(f"Sent back to Ping: {response}")


if __name__ == "__main__":
    main()
