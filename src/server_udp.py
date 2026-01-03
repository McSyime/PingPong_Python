#!/usr/bin/env python3
"""
Simple UDP Pong server.
Receives a number n and responds with n + 1.
"""

import socket  # Provides networking (socket) functionality

HOST = "127.0.0.1"  # localhost
PORT = 5000         # UDP port to listen on


def main():
    # Create a UDP socket (IPv4, datagram-based)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:

        # Bind the socket to the given host and port
        server_socket.bind((HOST, PORT))
        print(f"UDP Pong server listening on {HOST}:{PORT}")

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
