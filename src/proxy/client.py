#!/usr/bin/env python3
"""
Simple Ping client.
Sends an integer n to a proxy and prints the proxys response.
"""

import argparse  # Provides argument parser
import socket  # Provides networking (socket) functionality

DEFAULT_HOST = "127.0.0.1"  # Proxy server address
DEFAULT_PORT = 6000  # Proxy server port
NUMBER = 1  # Ping value (spin)


def parse_args():
    parser = argparse.ArgumentParser(description="TCP Ping Client")
    parser.add_argument(
        "--host",
        default=DEFAULT_HOST,
        help=f"Proxy host (default: {DEFAULT_HOST})"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=DEFAULT_PORT,
        help=f"Proxy port (default: {DEFAULT_PORT})"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    host = args.host
    port = args.port

    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to the Proxy server
        sock.connect((host, port))
        print(f"Connected to {host}:{port}")

        # Send the number to the proxy server
        message = str(NUMBER)
        sock.sendall(message.encode("utf-8"))
        print(f"Sent: {message}")

        # Receive the response from the proxy server
        data = sock.recv(1024)
        response = data.decode("utf-8")
        print(f"Received: {response}")


if __name__ == "__main__":
    main()
