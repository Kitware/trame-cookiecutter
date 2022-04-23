import multiprocessing

from {{cookiecutter.import_name}}.app import controller, ui

if __name__ == "__main__":
    multiprocessing.freeze_support()
    controller.on_start()
    ui.layout.start_desktop_window()
