#!/usr/bin/env python3
"""
Simple TCP Ping-Pong proxy.
Forwards data between client and Pong server without modifying it.
"""

import argparse  # Provides argument parser
import socket  # Provides networking (socket) functionality

# Proxy listens here (client connects to proxy)
DEFAULT_PROXY_HOST = "127.0.0.1"
DEFAULT_PROXY_PORT = 6000

# Actual Pong server
DEFAULT_SERVER_HOST = "127.0.0.1"
DEFAULT_SERVER_PORT = 5000


def parse_args():
    parser = argparse.ArgumentParser(description="Proxy Server")
    parser.add_argument(
        "--host",
        default=DEFAULT_PROXY_HOST,
        help=f"Host to bind to (default: {DEFAULT_PROXY_HOST})"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=DEFAULT_PROXY_PORT,
        help=f"Port to listen on (default: {DEFAULT_PROXY_PORT})"
    )
    parser.add_argument(
        "--pongHost",
        default=DEFAULT_SERVER_HOST,
        help=f"Pong server host (default: {DEFAULT_SERVER_HOST})"
    )
    parser.add_argument(
        "--pongPort",
        type=int,
        default=DEFAULT_SERVER_PORT,
        help=f"Pong server port (default: {DEFAULT_SERVER_PORT})"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    host = args.host
    port = args.port
    pong_host = args.pongHost
    pong_port = args.pongPort

    # Create TCP socket for proxy
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_socket:
        proxy_socket.bind((host, port))
        proxy_socket.listen()

        print(f"Ping-Pong proxy listening on {host}:{port}")
        print(f"Forwarding to Pong server at {pong_host}:{pong_port}")

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
                    server_conn.connect((pong_host, pong_port))

                    # Forward data to Pong server
                    server_conn.sendall(data)

                    # Receive response from Pong server
                    response = server_conn.recv(1024)

                print(f"Forwarding from server: {response.decode('utf-8').strip()}")

                # Send response back to client
                client_conn.sendall(response)


if __name__ == "__main__":
    main()
