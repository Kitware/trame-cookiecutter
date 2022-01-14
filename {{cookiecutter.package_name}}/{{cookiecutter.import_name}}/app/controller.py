r"""
Bind methods to the trame controller
"""

from trame import controller as ctrl, state
from . import engine


def bind_methods():
    ctrl.btn_click = engine.on_click
    ctrl.btn_reset = engine.on_reset
    ctrl.on_ready = engine.initialize
    ctrl.widget_click = engine.widget_click
    ctrl.widget_change = engine.widget_change


def bind_changes():
    state.change("my_title")(engine.title_change)
