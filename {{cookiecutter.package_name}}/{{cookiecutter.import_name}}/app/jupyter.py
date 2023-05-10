from .core import create_engine

def jupyter_proxy_info():
    """Get the config to run the trame application via jupyter's server proxy

    This is provided to the `jupyter_serverproxy_servers` entrypoint, and the
    jupyter server proxy will use it to start the application as a separate
    process.
    """
    return {
        "command": ["{{cookiecutter.entry_point}}", "-p", "0", "--server"],
    }


def show(server=None, **kwargs):
    """Show application into a Jupyter cell"""
    app = create_engine(server)
    app.show_in_jupyter(**kwargs)