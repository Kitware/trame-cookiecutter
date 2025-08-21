from trame.app import TrameApp
from trame.decorators import change, controller
from trame.ui.vuetify3 import SinglePageLayout
from trame.widgets import vuetify3, vtk
{%- if cookiecutter.include_components %}
from {{cookiecutter.import_name}}.widgets import {{cookiecutter.module_short_name}} as my_widgets
{%- endif %}


# ---------------------------------------------------------
# Engine class
# ---------------------------------------------------------

class MyTrameApp(TrameApp):
    def __init__(self, server=None):
        super().__init__(server, client_type="vue3")

        # --hot-reload arg optional logic
        if self.server.hot_reload:
            self.server.controller.on_server_reload.add(self._build_ui)

        # Set state variable
        self.state.trame__title = "{{cookiecutter.project_name}}"
        self.state.resolution = 6

        # build ui
        self._build_ui()

    @controller.set("reset_resolution")
    def reset_resolution(self):
        self.state.resolution = 6

    @change("resolution")
    def on_resolution_change(self, resolution, **kwargs):
        print(f">>> ENGINE(a): Slider updating resolution to {resolution}")

{%- if cookiecutter.include_components %}

    @controller.set("widget_click")
    def widget_click(self):
        print(">>> ENGINE(a): Widget Click")

    @controller.set("widget_change")
    def widget_change(self):
        print(">>> ENGINE(a): Widget Change")

{%- endif %}

    def _build_ui(self, *args, **kwargs):
        with SinglePageLayout(self.server) as self.ui:
            # Toolbar
            self.ui.title.set_text("Trame / vtk.js")
            with self.ui.toolbar:
                vuetify3.VSpacer()
{%- if cookiecutter.include_components %}
                my_widgets.CustomWidget(
                    attribute_name="Hello",
                    py_attr_name="World",
                    click=self.ctrl.widget_click,
                    change=self.ctrl.widget_change,
                )
                vuetify3.VSpacer()
{%- endif %}
                vuetify3.VSlider(                    # Add slider
                    v_model=("resolution", 6),      # bind variable with an initial value of 6
                    min=3, max=60, step=1,          # slider range
                    dense=True, hide_details=True,  # presentation setup
                )
                with vuetify3.VBtn(icon=True, click=self.ctrl.reset_camera):
                    vuetify3.VIcon("mdi-crop-free")
                with vuetify3.VBtn(icon=True, click=self.reset_resolution):
                    vuetify3.VIcon("mdi-undo")

            # Main content
            with self.ui.content:
                with vuetify3.VContainer(fluid=True, classes="pa-0 fill-height"):
                    with vtk.VtkView() as vtk_view:                # vtk.js view for local rendering
                        self.ctrl.reset_camera = vtk_view.reset_camera  # Bind method to controller
                        with vtk.VtkGeometryRepresentation():      # Add representation to vtk.js view
                            vtk.VtkAlgorithm(                      # Add ConeSource to representation
                                vtk_class="vtkConeSource",          # Set attribute value with no JS eval
                                state=("{ resolution }",)          # Set attribute value with JS eval
                            )

            # Footer
            # layout.footer.hide()
