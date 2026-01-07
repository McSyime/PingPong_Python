#!/usr/bin/env python3
"""
Simple Pong server.
Receives a number n and responds with n + 1.
"""

import argparse  # Provides argument parser
import socket  # Provides networking (socket) functionality

DEFAULT_HOST = "127.0.0.1"  # localhost
DEFAULT_PORT = 5000  # TCP port to listen on


def parse_args():
    parser = argparse.ArgumentParser(description="TCP Pong Server")
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

    # Create a TCP socket (IPv4, stream-based)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the given host and port
        server_socket.bind((host, port))

        # Start listening for incoming connections
        server_socket.listen()
        print(f"Pong server listening on {host}:{port}")

        # Server runs forever and handles one proxy at a time
        while True:
            # Wait for a proxy to connect
            conn, addr = server_socket.accept()
            print(f"Connection from {addr}")

            # Use 'with' to automatically close the connection
            with conn:
                # Receive up to 1024 bytes from the proxy
                data = conn.recv(1024)

                # If no data was received, the proxy closed the connection
                if not data:
                    print("No data received")
                    continue

                # Convert bytes to string and remove whitespace
                message = data.decode("utf-8").strip()
                print(f"Received: {message}")

                # Try to interpret the message as an integer
                try:
                    number = int(message)
                    response = str(number + 1)
                except ValueError:
                    # Message was not a valid integer
                    response = "ERROR"

                # Send the response back to the proxy
                conn.sendall(response.encode("utf-8"))
                print(f"Sent: {response}")


if __name__ == "__main__":
    main()
