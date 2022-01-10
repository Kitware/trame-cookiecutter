from trame import state, controller as ctrl
from trame.layouts import SinglePage
from trame.html import vuetify
{%- if cookiecutter.include_components %}
from {{cookiecutter.import_name}} import html as my_widgets
{%- endif %}

# Set value to state
state["my_title"] = "{{cookiecutter.project_name}}"

# Create single page layout type
# (FullScreenPage, SinglePage, SinglePageWithDrawer)
layout = SinglePage(
    "{{cookiecutter.project_name}}",
    on_ready=ctrl.on_ready,
)

# Toolbar
layout.title.set_text("{{cookiecutter.project_name}}")
with layout.toolbar as tb:
    vuetify.VSpacer()
{%- raw %}
    tb.add_child("{{ my_title }}") # Use string template to show my_title value
{%- endraw %}
    vuetify.VSpacer()
    vuetify.VBtn("Click me", click=ctrl.btn_click)

# Main content
with layout.content:
    with vuetify.VContainer(classes="fluid fill-height"):
        with vuetify.VRow():
            vuetify.VSpacer()
            vuetify.VBtn("Reset", click=ctrl.btn_reset)
            vuetify.VSpacer()
{%- if cookiecutter.include_components %}
        with vuetify.VRow():
            my_widgets.CustomWidget(
                attribute_name="Hello",
                py_attr_name="World",
                click=ctrl.widget_click,
                change=ctrl.widget_change,
            )
{%- endif %}

# Footer
# layout.footer.hide()
