#!/usr/bin/env python3
"""
Simple UDP Pong server.
Receives a number n and responds with n + 1.
"""

import argparse  # Provides argument parser
import socket  # Provides networking (socket) functionality

DEFAULT_HOST = "127.0.0.1"  # localhost
DEFAULT_PORT = 5000  # UDP port to listen on


def parse_args():
    parser = argparse.ArgumentParser(description="UDP Pong Server")
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

    # Create a UDP socket (IPv4, datagram-based)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:

        # Bind the socket to the given host and port
        server_socket.bind((host, port))
        print(f"UDP Pong server listening on {host}:{port}")

        # Server runs forever and handles incoming datagrams
        while True:
            # Receive data and client address
            data, addr = server_socket.recvfrom(1024)
            print(f"Packet received from {addr}")

            # Convert bytes to string and remove whitespace
            message = data.decode("utf-8").strip()
            print(f"Received: {message}")

            # Try to interpret the message as an integer
            try:
                number = int(message)
                response = str(number + 1)
            except ValueError:
                # Invalid data received
                response = "ERROR"

            # Send response back to the sender
            server_socket.sendto(response.encode("utf-8"), addr)
            print(f"Sent: {response}")


if __name__ == "__main__":
    main()
