{{ cookiecutter.project_name }}
----------------------------------------

{{ cookiecutter.short_description }}
{% if cookiecutter.is_open_source %}
License
----------------------------------------

This library is OpenSource and follow the {{ cookiecutter.license }}
{%- endif %}

Installation
----------------------------------------

Install the application/library

.. code-block:: console

    pip install {{ cookiecutter.package_name }}
{% if cookiecutter.include_app %}
Run the application

.. code-block:: console

    {{ cookiecutter.entry_point }}

{%- endif %}

Developement setup
----------------------------------------

We recommend using uv for setting up and managing a virtual environement for your development.

.. code-block:: console

    # Create venv and install all dependencies
    uv sync --all-extras --dev

    # Activate environement
    source .venv/bin/activate
{% if cookiecutter.include_ci %}
    # Install commit analysis
    pre-commit install
    pre-commit install --hook-type commit-msg
{%- endif %}

    # Allow live code edit
    uv pip install -e .

{% if cookiecutter.include_components %}
Build and install the Vue components

.. code-block:: console

    cd vue-components
    npm i
    npm run build
    cd -

{%- endif %}
{% if cookiecutter.include_ci %}
For running tests and checks, you can run ``nox``.

.. code-block:: console

    # run all
    nox

    # lint
    nox -s lint

    # tests
    nox -s tests
{%- endif %}

Professional Support
----------------------------------------

* `Training <https://www.kitware.com/courses/trame/>`_: Learn how to confidently use trame from the expert developers at Kitware.
* `Support <https://www.kitware.com/trame/support/>`_: Our experts can assist your team as you build your web application and establish in-house expertise.
* `Custom Development <https://www.kitware.com/trame/support/>`_: Leverage Kitware’s 25+ years of experience to quickly build your web application.
