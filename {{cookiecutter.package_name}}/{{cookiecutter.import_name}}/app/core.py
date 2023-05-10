r"""
Define your classes and create the instances that you need to expose
"""
import logging
from trame.app import get_server
from trame.ui.vuetify import SinglePageLayout
from trame.widgets import vuetify, vtk
{%- if cookiecutter.include_components %}
from {{cookiecutter.import_name}}.widgets import {{cookiecutter.import_name}} as my_widgets
{%- endif %}



logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# ---------------------------------------------------------
# Engine class
# ---------------------------------------------------------


class Engine:
    def __init__(self, server=None):
        if server is None:
            server = get_server()

        self._server = server

        # initialize state + controller
        state, ctrl = server.state, server.controller

        # Set state variable
        state.trame__title = "{{cookiecutter.project_name}}"
        state.resolution = 6

        # Bind instance methods to controller
        ctrl.reset_resolution = self.reset_resolution
        ctrl.on_server_reload = self.ui
{%- if cookiecutter.include_components %}
        ctrl.widget_click = self.widget_click
        ctrl.widget_change = self.widget_change
{%- endif %}

        # Bind instance methods to state change
        state.change("resolution")(self.on_resolution_change)

        # Generate UI
        self.ui()

    @property
    def server(self):
        return self._server

    @property
    def state(self):
        return self.server.state

    @property
    def ctrl(self):
        return self.server.controller

    def show_in_jupyter(self, **kwargs):
        from trame.app import jupyter

        logger.setLevel(logging.WARNING)
        jupyter.show(self.server, **kwargs)


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

    def ui(self, *args, **kwargs):
        with SinglePageLayout(self._server) as layout:
            # Toolbar
            layout.title.set_text("Trame / vtk.js")
            with layout.toolbar:
                vuetify.VSpacer()
{%- if cookiecutter.include_components %}
                my_widgets.CustomWidget(
                    attribute_name="Hello",
                    py_attr_name="World",
                    click=self.ctrl.widget_click,
                    change=self.ctrl.widget_change,
                )
                vuetify.VSpacer()
{%- endif %}
                vuetify.VSlider(                    # Add slider
                    v_model=("resolution", 6),      # bind variable with an initial value of 6
                    min=3, max=60,                  # slider range
                    dense=True, hide_details=True,  # presentation setup
                )
                with vuetify.VBtn(icon=True, click=self.ctrl.reset_camera):
                    vuetify.VIcon("mdi-crop-free")
                with vuetify.VBtn(icon=True, click=self.ctrl.reset_resolution):
                    vuetify.VIcon("mdi-undo")

            # Main content
            with layout.content:
                with vuetify.VContainer(fluid=True, classes="pa-0 fill-height"):
                    with vtk.VtkView() as vtk_view:                # vtk.js view for local rendering
                        self.ctrl.reset_camera = vtk_view.reset_camera  # Bind method to controller
                        with vtk.VtkGeometryRepresentation():      # Add representation to vtk.js view
                            vtk.VtkAlgorithm(                      # Add ConeSource to representation
                                vtk_class="vtkConeSource",          # Set attribute value with no JS eval
                                state=("{ resolution }",)          # Set attribute value with JS eval
                            )

            # Footer
            # layout.footer.hide()


def create_engine(server=None):
    # Get or create server
    if server is None:
        server = get_server()

    if isinstance(server, str):
        server = get_server(server)

    return Engine(server)