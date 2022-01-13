r"""
Bind methods to the trame controller
"""

from trame import controller as ctrl
from .engine import initialize, on_click, on_reset, widget_click, widget_change


def bind_methods():
    ctrl.btn_click = on_click
    ctrl.btn_reset = on_reset
    ctrl.on_ready = initialize
    ctrl.widget_click = widget_click
    ctrl.widget_change = widget_change
