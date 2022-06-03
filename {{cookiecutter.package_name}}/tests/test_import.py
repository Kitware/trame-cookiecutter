def test_import():
{%- if cookiecutter.include_app %}
    from {{ cookiecutter.import_name }} import main  # noqa: F401
{%- endif %}
{%- if cookiecutter.include_components %}
    from {{ cookiecutter.import_name }}.widgets.{{ cookiecutter.import_name }} import CustomWidget  # noqa: F401
{%- endif %}
{%- if cookiecutter.include_components_only %}

    # For components only, the CustomWidget is also importable via trame
    from trame.widgets.{{ cookiecutter.import_name }} import CustomWidget  # noqa: F401,F811
{%- endif %}
