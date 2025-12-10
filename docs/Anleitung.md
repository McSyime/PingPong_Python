# Einführung
Das Ziel dieses Projekts ist es, ein Pingpong-Spiel in Python zu programmieren. Wir möchten dieses Projekt mit einer VM unter Debian realisieren. Es wird auf einem TCP/UDP-Protokoll basieren.

## Hardware 
Als Hardware benötigen wir lediglich unseren PC, da wir die Anwendung nicht auf einem externen Server ausführen möchten. 

## Software 
Als Software benötigen wir Oracle VirtualBox, um unsere Debian-VM auszuführen. Wir verwenden Github als Datenzentrum (Code und Dokumentation), Python als Programmiersprache und Git, um die Versionen unseres Projekts zu verfolgen. 

## Methodik 
Wir möchten, dass das gesamte Programm auf einem einzigen Rechner laufen kann. Das heisst, dass Ping und Pong lokal ohne externe Kommunikation laufen. Um dieses Schema zu realisieren, verwenden wir die Adresse 127.0.0.1 und den Port 5000 unseres Rechners. 
