{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.short_description }}

{% if cookiecutter.is_open_source %}
* Free software: {{ cookiecutter.license }}
{% endif %}

Installing
----------

{%- if cookiecutter.include_components %}
Build and install the Vue components

.. code-block:: console

    cd vue-components
    npm i
    npm run build
    cd -

{%- endif %}

Install the application

.. code-block:: console

    pip install -e .

{% if cookiecutter.include_app %}
Run the application

.. code-block:: console

    {{ cookiecutter.entry_point }}

{%- endif %}

Features
--------

* TODO
