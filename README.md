# Ping Pong Protocol – Client / Server (Python)
Einfaches Client/Server-Projekt in Python.
Der Client sendet eine ganze Zahl `n` an den Server.
Der Server antwortet mit `n + 1`.

## Zielen des Projekt 
- Die Grundlagen der Netzwerkkommunikation verstehen
- Ein einfaches Protokoll implementieren
- Lernen, wie man ein Client/Server-Projekt strukturiert
- Mit Git, Terminal und GNU/Linux arbeiten

## Architektur
client/
- client.py
- README.md

server/
- server.py
- README.md

docs/
- protocol.md
- README.md

## Voraussetzungen
- Python 3.14
- 2x VM Debian 

## Server und Client starten

'python server/server.py'
'python client/client.py' 

## Geplante Entwicklungen
- Strukturierte Nachrichten (JSON)
- Fehlerbehandlung
- Serverprotokolle
- Automatisierte Tests

## Workflow Git
- main: stabile Version
- develop: Entwicklung
- feature/*: neue Funktionen

## ACK- und NACK-Antworten
Zur Fehlerbehandlung werden zwei Arten von Antworten verwendet:

- ACK (Acknowledgement): Bestätigt, dass die Nachricht korrekt empfangen und verarbeitet wurde. In diesem Fall sendet der Server das Ergebnis (Zahl + 1) zurück.
-  NACK (Negative Acknowledgement): Meldet, dass ein Fehler in der Nachricht erkannt wurde, zum Beispiel eine falsche Prüfsumme.

Erhält der Client eine NACK-Antwort oder innerhalb einer bestimmten Zeit keine Antwort (Timeout), wird die Nachricht erneut gesendet. Das Timeout beginnt unmittelbar nachdem der Client eine Nachricht an den Server gesendet hat und auf eine Antwort wartet. Wird innerhalb dieser Zeit keine ACK- oder NACK-Antwort empfangen, gilt die Nachricht als verloren und wird erneut gesendet. Dadurch wird trotz der Verwendung von UDP eine einfache Zuverlässigkeit erreicht.
