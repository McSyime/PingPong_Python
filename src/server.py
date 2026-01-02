#!/usr/bin/env python3
"""
Simple Pong server.
Receives a number n and responds with n + 1.
"""
 
import socket  # Provides networking (socket) functionality
 
HOST = "127.0.0.1"  # localhost
PORT = 5000        # TCP port to listen on
 
def main():
    # Create a TCP socket (IPv4, stream-based)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the given host and port
        server_socket.bind((HOST, PORT))

        # Start listening for incoming connections
        server_socket.listen()
        print(f"Pong server listening on {HOST}:{PORT}")

        # Server runs forever and handles one client at a time
        while True:
            # Wait for a client to connect
            conn, addr = server_socket.accept()
            print(f"Connection from {addr}")

            # Use 'with' to automatically close the connection
            with conn:
                # Receive up to 1024 bytes from the client
                data = conn.recv(1024)

                # If no data was received, the client closed the connection
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

                # Send the response back to the client
                conn.sendall(response.encode("utf-8"))
                print(f"Sent: {response}")
 
if __name__ == "__main__":
    main()
