# Dokumentation

## Git repository klonen

Das Git repository mit folgendem Befehl klonen.

```
git clone https://github.com/McSyime/PingPong_Python.git
```

## Anleitung zur Nutzung des Programms

### Kommandozeilen-Parameter

Standardmäßig werden folgende Werte verwendet:

- Host: 127.0.0.1
- Port: 5000

Abhängig vom Feature können zusätzliche Parameter vorhanden sein, z. B. Host und Port für Proxy-Server.

Diese Standard-Werte können in allen Programmen über Kommandozeilen-Parameter angepasst werden.
Die jeweils verfügbaren Optionen können mit `-h` oder `--help` angezeigt werden.
So kann beispielsweise mit folgendem Befehl der Host und Port mitgegeben werden:

```
python3 server.py --host=127.0.0.1 --port=6000
```

**Hinweis:**  
Wird der Server mit einem anderen Host oder Port gestartet, müssen dieselben Werte auch beim Start des Clients angegeben
werden, damit sich Client und Server korrekt verbinden können.

### 1.1.1 Basic Ping-Pong

Ping sendet eine Zahl *n* und Pong antwortet mit *n* + 1.

1. In das Verzeichnis **PingPong_Python/src/basic** wechseln:

```
cd PingPong_Python/src/basic
```

2. Den Server **server.py** starten:

```
python3 server.py
```

3. In einem zweiten Terminal den Client **client.py** starten.

```
python3 client.py
```

### 1.1.2 Ping-Pong mit UDP Fehlerbehandlung

Diese Variante verwendet UDP anstelle von TCP. Da UDP keine zuverlässige Zustellung garantiert, implementiert der Client
eine einfache Fehlerbehandlung mittels Timeout. Ein Fehler kann beispielsweise erzeugt werden, indem nur der Client
gestartet wird oder dem Client ein anderer Host bzw. Port übergeben wird als dem Server.

1. In das Verzeichnis **PingPong_Python/src/udp** wechseln:

```
cd PingPong_Python/src/udp
```

2. Den Server **server.py** starten:

```
python3 server.py
```

3. In einem zweiten Terminal den Client **client.py** starten.

```
python3 client.py
```

### 1.1.3 Ping-Pong mit einem Ping-Pong Proxy

In dieser Variante wird ein Proxy zwischen Client und Pong-Server geschaltet. Der Client sendet eine Zahl n an den
Proxy, der die Nachricht an den Pong-Server weiterleitet. Der Pong-Server antwortet mit n + 1, und der Proxy leitet die
Antwort zurück an den Client.

1. In das Verzeichnis **PingPong_Python/src/proxy** wechseln:

```
cd PingPong_Python/src/proxy
```

2. Den Server **server.py** starten:

```
python3 server.py
```

3. In einem zweiten Terminal den Proxy-Server **proxy_server.py** starten.

```
python3 proxy_server.py
```

4. In einem dritten Terminal den Client **client.py** starten.

```
python3 client.py
```

### 1.1.4 Kette von Ping-Pongs

### 1.1.5 Ping-Pong in einer Stern Topologie

### 1.1.6 Ping-Pong in einer vermaschten Topologie
In dieser Umsetzung wird eine Stern-Topologie verwendet, bei der der Hub den zentralen Knoten bildet.
Der Client (Ping) verbindet sich ausschliesslich mit dem Hub und nicht direkt mit den einzelnen Servern.

Der Hub kennt die Ports aller Pang- und Pong-Server und leitet die empfangene Zahl in einer fest definierten Reihenfolge (statisches Routing) an diese weiter.
Die verwendeten Ports können bei Bedarf angepasst werden, wodurch die Topologie flexibel konfigurierbar ist.

Jeder Pang- und Pong-Server erhöht die empfangene Zahl um +1 und sendet das Ergebnis an den Hub zurück.
Der Hub sammelt die Antworten und sendet erst am Ende das Endergebnis an den Client zurück.
