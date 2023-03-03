from trame.app import get_server
from .core import Engine


def main(server=None, **kwargs):
    # Get or create server
    if server is None:
        server = get_server()

    if isinstance(server, str):
        server = get_server(server)

    # Init application
    Engine(server)

    # Start server
    server.start(**kwargs)


if __name__ == "__main__":
    main()
