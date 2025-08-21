================{% for _ in cookiecutter.project_name %}={% endfor %}
Contributing to {{ cookiecutter.project_name }}
================{% for _ in cookiecutter.project_name %}={% endfor %}

#. Clone the repository using ``git clone``
{%- if cookiecutter.include_ci %}
#. Install pre-commit via ``pip install pre-commit``
#. Run ``pre-commit install`` to set up pre-commit hooks
#. Run ``pre-commit install --hook-type commit-msg`` to register commit-msg hook
{%- endif %}
#. Make changes to the code, and commit your changes to a separate branch
#. Create a fork of the repository on GitHub
#. Push your branch to your fork, and open a pull request
{%- if cookiecutter.include_ci %}

Tips
####

#. When first creating a new project, it is helpful to run ``pre-commit run --all-files`` to ensure all files pass the pre-commit checks.
#. A quick way to fix ``ruff`` issues is by installing ruff (``pip install ".[dev]"``) and running the ``ruff check --fix`` command at the root of your repository.
#. A quick way to fix ``codespell`` issues is by installing codespell (``pip install codespell``) and running the ``codespell -w`` command at the root of your directory.
#. The `.codespellrc file <https://github.com/codespell-project/codespell#using-a-config-file>`_ can be used fix any other codespell issues, such as ignoring certain files, directories, words, or regular expressions.
{%- endif %}
