from .controller import bind_changes, bind_methods
from .ui import layout


def start_server():
    layout.start()


def start_desktop():
    layout.start_desktop_window()


def main():
    bind_changes()
    bind_methods()
    start_server()


if __name__ == "__main__":
    main()
