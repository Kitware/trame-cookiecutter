import asyncio

from trame import port
from trame.jupyter import display_iframe

from {{cookiecutter.import_name}}.app import controller, ui


def run_in_loop(**kwargs):
    """Run and display the trame application in jupyter's event loop

    The kwargs are forwarded to IPython.display.IFrame()
    """
    controller.on_start()
    ui.layout.start(exec_mode="task", server=True)

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
