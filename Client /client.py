#!/usr/bin/env python3
"""
Einfacher Ping-Client für das Ping-Pong-Projekt.
Verbindet sich mit dem Pong-Server, schickt eine Zahl n
und zeigt die Antwort (n+1) an.
"""
 
import socket  # Netzwerkmodul
 
HOST = "127.0.0.1"  # Muss zum Server passen
PORT = 5000        # Muss zum Server-Port passen
 
def main():
    # 1) Socket für TCP-Verbindung zum Server erstellen
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # 2) Mit Server verbinden
        sock.connect((HOST, PORT))
        print(f"Verbunden mit Pong-Server {HOST}:{PORT}")
 
        while True:
            # 3) Benutzer nach einer Zahl fragen
            user_input = input("Zahl zum Pingen (oder 'exit' zum Beenden): ").strip()
 
            # 4) Möglichkeit zum Beenden
            if user_input.lower() in ("exit", "quit"):
                print("Beende Client.")
                break
 
            # 5) Eingabe an den Server schicken
            #    + '\n', damit wir serverseitig schön strippen können
            message = user_input + "\n"
            sock.sendall(message.encode("utf-8"))
 
            # 6) Antwort vom Server lesen
            data = sock.recv(1024)
 
            if not data:
                print("Server hat die Verbindung beendet.")
                break
 
            response_text = data.decode("utf-8").strip()
            print("Antwort (Pong):", response_text)
 
if __name__ == "__main__":
    main()
