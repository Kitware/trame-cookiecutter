import controller # noqa
from ui import layout

def start_server():
    layout.start()

def start_desktop():
    layout.start_desktop_window()

if __name__ == "__main__":
    start_server()