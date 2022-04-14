r"""
Define your classes and create the instances that you need to expose
"""
import logging

from trame import state

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# ---------------------------------------------------------
# Methods
# ---------------------------------------------------------

def initialize():
    logger.info(">>> ENGINE: Application initialize only once")

def protocols_ready():
    logger.info(">>> ENGINE: Server protocols initialized / Client not connected yet")

def reset_resolution():
    state.resolution = 6

{%- if cookiecutter.include_components %}
def widget_click():
    logger.info(">>> ENGINE: Widget Click")

def widget_change():
    logger.info(">>> ENGINE: Widget Change")

{%- endif %}

# ---------------------------------------------------------
# Listeners
# ---------------------------------------------------------

@state.change("resolution")
def resolution_changed(resolution, **kwargs):
    logger.info(f">>> ENGINE: Slider updating resolution to {resolution}")
