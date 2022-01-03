from trame.app import get_server, dev
from . import engine, ui

def _reload():
    server = get_server()
    dev.reload(ui)
    ui.initialize(server)


def main(**kwargs):
    server = get_server()

    # Make UI auto reload
    server.controller.on_server_reload.add(_reload)

    # Init application
    engine.initialize(server)
    ui.initialize(server)

    # Start server
    server.start(**kwargs)


if __name__ == "__main__":
    main()
