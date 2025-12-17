#!/usr/bin/env python3
"""
Einfacher Pong-Server für das Ping-Pong-Projekt.
Erwartet von einem Client eine Zahl n und antwortet mit n+1.
"""
 
import socket  # Modul für Netzwerk / Sockets
 
HOST = "127.0.0.1"  # 127.0.0.1 = localhost (eigener Rechner)
PORT = 5000        # Beliebiger Port > 1024, solange frei
 
def main():
    # 1) Socket erzeugen: AF_INET = IPv4, SOCK_STREAM = TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # 2) Socket an Adresse (HOST, PORT) binden
        server_socket.bind((HOST, PORT))
 
        # 3) Auf eingehende Verbindungen warten
        server_socket.listen()
        print(f"Pong-Server läuft auf {HOST}:{PORT} ...")
 
        while True:
            # 4) Auf einen Client warten (blockiert bis sich jemand verbindet)
            conn, addr = server_socket.accept()
            print(f"Neue Verbindung von {addr}")
 
            # 'with' sorgt dafür, dass die Verbindung sauber geschlossen wird
            with conn:
                while True:
                    # 5) Daten vom Client lesen (max 1024 Bytes)
                    data = conn.recv(1024)
 
                    # Wenn nichts mehr kommt: Client hat Verbindung beendet
                    if not data:
                        print("Client hat die Verbindung geschlossen.")
                        break
 
                    # 6) Bytes -> Text (String)
                    text = data.decode("utf-8").strip()
                    print(f"Vom Client empfangen: {text}")
 
                    # 7) Versuchen, die empfangene Nachricht als Zahl zu interpretieren
                    try:
                        n = int(text)
                        result = n + 1
                        response_text = f"{result}\n"
                        print(f"Sende zurück: {result}")
                    except ValueError:
                        # Wenn keine Zahl -> Fehlermeldung
                        response_text = "FEHLER: Bitte eine ganze Zahl schicken\n"
                        print("Keine gültige Zahl erhalten, sende Fehlermeldung.")
 
                    # 8) Antwort zurück an den Client schicken
                    conn.sendall(response_text.encode("utf-8"))
 
if __name__ == "__main__":
    main()
