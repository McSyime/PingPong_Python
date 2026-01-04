#!/usr/bin/env python3
"""
Simple Ping client.
Sends an integer n to a proxy and prints the proxys response.
"""

import socket  # Provides networking (socket) functionality

HOST = "127.0.0.1"  # Proxy server address
PORT = 6000  # Proxy server port
NUMBER = 1  # Ping value (spin)


def main():
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to the Proxy server
        sock.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")

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
