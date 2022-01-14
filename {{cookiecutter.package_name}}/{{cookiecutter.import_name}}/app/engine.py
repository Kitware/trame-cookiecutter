r"""
Define your classes and create the instances that you need to expose
"""
from trame import state

# ---------------------------------------------------------
# Methods
# ---------------------------------------------------------


def initialize():
    print("Application starting: Layout(on_ready=xxx)")


def on_click():
    print("Click")
    state.my_title = state.my_title[::-1]


def on_reset():
    print("Reset")


def widget_click():
    print("Widget Click")


def widget_change():
    print("Widget Change")


# ---------------------------------------------------------
# Listeners
# ---------------------------------------------------------


def title_change(my_title, **kwargs):
    print(f" => title changed to {my_title}")
