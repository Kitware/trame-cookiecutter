r"""
Define your classes and create the instances that you need to expose
"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# ---------------------------------------------------------
# Engine class
# ---------------------------------------------------------


class MyBusinessLogic:
    def __init__(self, server):
        self._server = server

        # initialize state + controller
        state, ctrl = server.state, server.controller
        state.resolution = 6
        ctrl.reset_resolution = self.reset_resolution
        state.change("resolution")(self.on_resolution_change)
{%- if cookiecutter.include_components %}
        ctrl.widget_click = self.widget_click
        ctrl.widget_change = self.widget_change
{%- endif %}

    def reset_resolution(self):
        self._server.state.resolution = 6

    def on_resolution_change(self, resolution, **kwargs):
        logger.info(f">>> ENGINE(a): Slider updating resolution to {resolution}")

{%- if cookiecutter.include_components %}

    def widget_click(self):
        logger.info(">>> ENGINE(a): Widget Click")

    def widget_change(self):
        logger.info(">>> ENGINE(a): Widget Change")

{%- endif %}


# ---------------------------------------------------------
# Server binding
# ---------------------------------------------------------


def initialize(server):
    state, ctrl = server.state, server.controller

    @state.change("resolution")
    def resolution_changed(resolution, **kwargs):
        logger.info(f">>> ENGINE(b): Slider updating resolution to {resolution}")

    def protocols_ready(**initial_state):
        logger.info(f">>> ENGINE(b): Server is ready {initial_state}")

    ctrl.on_server_ready.add(protocols_ready)

    engine = MyBusinessLogic(server)
    return engine
