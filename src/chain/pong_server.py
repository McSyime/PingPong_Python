#!/usr/bin/env python3
"""
Pong server.
Receives a number, increments it, and sends it back to Pang.
"""

import socket

HOST = "127.0.0.1"
PORT = 5001  # Pong listens here


def main():
    # Create a TCP socket (IPv4, stream-based)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the given host and port
        server_socket.bind((HOST, PORT))

        # Start listening for incoming connections
        server_socket.listen()
        print(f"Pong server listening on {HOST}:{PORT}")

        while True:
            # Wait for a pang server to connect
            conn, addr = server_socket.accept()
            print(f"Connection from Pang {addr}")

            # Use 'with' to automatically close the connection
            with conn:
                # Receive up to 1024 bytes from the pang server
                data = conn.recv(1024)

                # If no data was received, the pang server closed the connection
                if not data:
                    print("No data received")
                    continue

                # Convert bytes to string and remove whitespace
                message = data.decode("utf-8").strip()
                print(f"Received from Pang: {message}")

                # Try to interpret the message as an integer
                try:
                    number = int(message)
                    response = str(number + 1)
                except ValueError:
                    # Message was not a valid integer
                    response = "ERROR"

                # Send the response back to the pang server
                conn.sendall(response.encode("utf-8"))
                print(f"Sent back to Pang: {response}")


if __name__ == "__main__":
    main()
