#!/usr/bin/env python3
"""
Simple TCP Ping-Pong proxy.
Forwards data between client and Pong server without modifying it.
"""

import socket

# Proxy listens here (client connects to proxy)
PROXY_HOST = "127.0.0.1"
PROXY_PORT = 6000

# Actual Pong server
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000


def main():
    # Create TCP socket for proxy
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_socket:
        proxy_socket.bind((PROXY_HOST, PROXY_PORT))
        proxy_socket.listen()

        print(f"Ping-Pong proxy listening on {PROXY_HOST}:{PROXY_PORT}")
        print(f"Forwarding to Pong server at {SERVER_HOST}:{SERVER_PORT}")

        while True:
            # Wait for client connection
            client_conn, client_addr = proxy_socket.accept()
            print(f"Client connected from {client_addr}")

            with client_conn:
                # Receive data from client
                data = client_conn.recv(1024)
                if not data:
                    print("No data received from client")
                    continue

                print(f"Forwarding from client: {data.decode('utf-8').strip()}")

                # Connect to the real Pong server
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_conn:
                    server_conn.connect((SERVER_HOST, SERVER_PORT))

                    # Forward data to Pong server
                    server_conn.sendall(data)

                    # Receive response from Pong server
                    response = server_conn.recv(1024)

                print(f"Forwarding from server: {response.decode('utf-8').strip()}")

                # Send response back to client
                client_conn.sendall(response)


if __name__ == "__main__":
    main()
