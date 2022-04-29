import asyncio

from trame import port
from trame.jupyter import display_iframe

from {{cookiecutter.import_name}}.app import controller, ui


# Keep track of whether we have ran this function before
FIRST_RUN = True


def run_in_loop(**kwargs):
    """Run and display the trame application in jupyter's event loop

    The kwargs are forwarded to IPython.display.IFrame()
    """
    global FIRST_RUN
    if FIRST_RUN:
        # Disable info logging for the engine logger
        import logging
        engine_logger = logging.getLogger("{{cookiecutter.import_name}}.app.engine")
        engine_logger.setLevel(logging.WARNING)

        # Start up trame
        controller.on_start()
        ui.layout.start(exec_mode="task", server=True, port=0)

        FIRST_RUN = False

    def display():
        src = f"http://localhost:{port()}"
        display_iframe(src, **kwargs)

    # Give wslink a tiny bit of time to get started
    loop = asyncio.get_event_loop()
    loop.call_later(0.1, display)


def jupyter_proxy_info():
    """Get the config to run the trame application via jupyter's server proxy

    This is provided to the `jupyter_serverproxy_servers` entrypoint, and the
    jupyter server proxy will use it to start the application as a separate
    process.
    """
    return {
        'command': ['{{cookiecutter.entry_point}}', '-p', '{port}', '--server'],
    }
