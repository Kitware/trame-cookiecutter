r"""
Bind methods to the trame controller
"""

from trame import controller as ctrl
from . import engine


def bind_methods():
    ctrl.on_ready = engine.protocols_ready
    ctrl.reset_resolution = engine.reset_resolution
{%- if cookiecutter.include_components %}
    ctrl.widget_click = engine.widget_click
    ctrl.widget_change = engine.widget_change
{%- endif %}

def on_start():
    """Method called for initialization when the application starts"""
    engine.initialize()
    bind_methods()


def on_reload(reload_modules):
    """Method called when the module is reloaded

    reload_modules is a function that takes modules to reload

    We only need to reload the controller if the engine is reloaded.
    """
    # reload_modules(engine)
    bind_methods()
