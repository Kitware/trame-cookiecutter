{%- if cookiecutter.include_app -%}
from .app import main

__all__ = [
    "main",
]
{%- endif -%}
