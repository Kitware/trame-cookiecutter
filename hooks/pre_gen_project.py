#!/usr/bin/env python3

# Run some code (such as validation) before generation

import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
import_name = '{{ cookiecutter.import_name }}'


# Perform validation
if not re.match(MODULE_REGEX, import_name):
    msg = (
        f'ERROR: The import name {import_name} is not a valid Python module '
        'name.'
    )
    if '-' in import_name:
        msg += ' Be sure to use "_" instead of "-".'

    sys.exit(msg)

# Set some convenience cookie cutter variables
{% set _ = cookiecutter.update({
    'vue_prefix': 'your',
    'entry_point': cookiecutter.package_name,
    'is_known_license': cookiecutter.license != 'Other',
    'is_open_source': cookiecutter.license != 'Other',
    'include_app': cookiecutter.project_type != 'Components',
    'include_components': cookiecutter.project_type != 'App',
    'include_components_only': cookiecutter.project_type == 'Components',
    'include_ci': cookiecutter.include_continuous_integration == 'y',
}) %}
