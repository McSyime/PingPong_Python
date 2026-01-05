#!/usr/bin/env python3
"""
Pang server.
Forwards data between Ping and Pong and increments the value.
"""

import socket

# Pang listens here (Ping connects here)
HOST = "127.0.0.1"
PORT = 5000

# Pong server address
PONG_HOST = "127.0.0.1"
PONG_PORT = 5001


def main():
    # Create a TCP socket (IPv4, stream-based)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as pang_socket:
        # Bind the socket to the given host and port
        pang_socket.bind((HOST, PORT))

        # Start listening for incoming connections
        pang_socket.listen()
        print(f"Pang server listening on {HOST}:{PORT}")

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
                    pong_conn.connect((PONG_HOST, PONG_PORT))
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
