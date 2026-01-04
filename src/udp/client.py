#!/usr/bin/env python3
"""
Simple UDP Ping client.
Sends an integer n and prints the server response.
"""

import socket  # Provides networking (socket) functionality

HOST = "127.0.0.1"  # Server address
PORT = 5000         # Server port
NUMBER = 1          # Ping value (spin)
TIMEOUT = 2         # Timeout in seconds


def main():
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:

        # Set a timeout to handle missing responses
        sock.settimeout(TIMEOUT)

        message = str(NUMBER)
        sock.sendto(message.encode("utf-8"), (HOST, PORT))
        print(f"Sent: {message}")

        try:
            # Wait for response from server
            data, addr = sock.recvfrom(1024)
            response = data.decode("utf-8")
            print(f"Received from {addr}: {response}")
        except socket.timeout:
            # No response received within timeout
            print("ERROR: No response from server (timeout)")

        except ConnectionResetError:
            # Happens on Windows if no server is listening
            print("ERROR: Server unreachable (no UDP listener)")

if __name__ == "__main__":
    main()
