import argparse
import socket

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 5005  # Hub-Port

DEFAULT_ROUTE = [
    ("Pang1", "127.0.0.1", 5000),
    ("Pong1", "127.0.0.1", 5001),
    ("Pang2", "127.0.0.1", 5002),
    ("Pong2", "127.0.0.1", 5003),
]


def parse_args():
    parser = argparse.ArgumentParser(description="Hub")
    parser.add_argument(
        "--host",
        default=DEFAULT_HOST,
        help=f"Host to bind to (default: {DEFAULT_HOST})"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=DEFAULT_PORT,
        help=f"Port to listen on (default: {DEFAULT_PORT})"
    )
    parser.add_argument(
        "--node",
        action="append",
        help=(
            "Routing node in format Name:Host:Port. "
            "If at least one --node is specified, the complete default route is replaced. "
            "In this case, all routing nodes must be provided explicitly and in order."
        )
    )
    return parser.parse_args()


def parse_route(node_args):
    route = []
    for node in node_args:
        try:
            name, host, port = node.split(":")
            route.append((name, host, int(port)))
        except ValueError:
            raise ValueError(
                f"Invalid --node format: '{node}', expected Name:Host:Port"
            )
    return route


def call_node(host, port, value):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(str(value).encode("utf-8"))
        data = s.recv(1024)
    return int(data.decode("utf-8").strip())


def main():
    args = parse_args()
    host = args.host
    port = args.port
    if args.node:
        route = parse_route(args.node)
        print("Using custom route:")
    else:
        route = DEFAULT_ROUTE
        print("Using default route:")
    for name, h, p in route:
        print(f"  - {name} ({h}:{p})")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as hub:
        hub.bind((host, port))
        hub.listen()
        print(f"Hub listening on {host}:{port}")

        while True:
            conn, addr = hub.accept()
            with conn:
                data = conn.recv(1024)
                value = int(data.decode("utf-8").strip())
                print(f"[Hub] Start: {value}")

                for name, h, p in route:
                    old = value
                    value = call_node(h, p, value)
                    print(f"[Hub] {name}: {old} -> {value}")

                conn.sendall(str(value).encode("utf-8"))
                print(f"[Hub] Final result sent: {value}")


if __name__ == "__main__":
    main()
