r"""
Bind methods to the trame controller
"""

from trame import controller as ctrl
from . import engine


def bind_methods():
    ctrl.btn_click = engine.on_click
    ctrl.btn_reset = engine.on_reset
    ctrl.on_ready = engine.initialize
    ctrl.widget_click = engine.widget_click
    ctrl.widget_change = engine.widget_change


def on_start():
    """Method called for initialization when the application starts"""
    bind_methods()


def on_reload(reload_modules):
    """Method called when the module is reloaded

    reload_modules is a function that takes modules to reload

    We only need to reload the controller if the engine is reloaded.
    """
    # reload_modules(engine)
    bind_methods()
