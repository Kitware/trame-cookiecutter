from trame import state, controller as ctrl
from trame.layouts import SinglePage
from trame.html import vuetify, vtk
{%- if cookiecutter.include_components %}
from {{cookiecutter.import_name}} import html as my_widgets
{%- endif %}

# Create single page layout type
# (FullScreenPage, SinglePage, SinglePageWithDrawer)
layout = SinglePage(
    "{{cookiecutter.project_name}}",
    on_ready=ctrl.on_ready,
)

# Toolbar
layout.title.set_text("Trame / vtk.js")
with layout.toolbar as tb:
    vuetify.VSpacer()
{%- if cookiecutter.include_components %}
    my_widgets.CustomWidget(
        attribute_name="Hello",
        py_attr_name="World",
        click=ctrl.widget_click,
        change=ctrl.widget_change,
    )
    vuetify.VSpacer()
{%- endif %}
    vuetify.VSlider(                # Add slider
        v_model=("resolution", 6),     # bind variable with an initial value of 6
        min=3, max=60,                 # slider range
        dense=True, hide_details=True, # presentation setup
    )
    with vuetify.VBtn(icon=True, click=ctrl.reset_camera):
        vuetify.VIcon("mdi-crop-free")
    with vuetify.VBtn(icon=True, click=ctrl.reset_resolution):
        vuetify.VIcon("mdi-undo")


# Main content
with layout.content:
    with vuetify.VContainer(fluid=True, classes="pa-0 fill-height"):
        with vtk.VtkView() as vtk_view:               # vtk.js view for local rendering
            ctrl.reset_camera = vtk_view.reset_camera # Bind method to controller
            with vtk.VtkGeometryRepresentation():     # Add representation to vtk.js view
                vtk.VtkAlgorithm(                     # Add ConeSource to representation
                    vtkClass="vtkConeSource",           # Set attribute value with no JS eval
                    state=("{ resolution }",)           # Set attribute value with JS eval
                )

# Footer
# layout.footer.hide()
