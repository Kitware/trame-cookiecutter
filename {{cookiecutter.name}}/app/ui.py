from trame import controller as ctrl
from trame.layouts import SinglePage
from trame.html import vuetify
from .. import html as my_widgets

# Create single page layout type (FullScreenPage, SinglePage, SinglePageWithDrawer)
layout = SinglePage(
    "{{cookiecutter.title}}", 
    on_ready=ctrl.on_ready,
)

# Toolbar
layout.title.set_text("{{cookiecutter.title}}")
with layout.toolbar:
    vuetify.VSpacer()
    vuetify.VBtn("Click me", click=ctrl.btn_click)

# Main content
with layout.content:
    with vuetify.VContainer(classes="fluid fill-height"):
        with vuetify.VRow():
            vuetify.VSpacer()
            vuetify.VBtn("Reset", click=ctrl.btn_reset)
            vuetify.VSpacer()
        with vuetify.VRow():
            my_widgets.CustomWidget(
                attribute_name="Hello",
                py_attr_name="World",
                click=ctrl.widget_click,
                change=ctrl.widget_change,
            )


# Footer
# layout.footer.hide()