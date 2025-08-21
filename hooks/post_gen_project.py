#!/usr/bin/env python

from pathlib import Path
import shutil

PROJECT_DIRECTORY = Path.cwd()


def remove_files(*paths):
    for path in paths:
        Path(path).unlink()

def remove_dirs(*paths):
    for path in paths:
        shutil.rmtree(path)


if not {{ cookiecutter.is_known_license }}:
    remove_files('LICENSE')

if not {{ cookiecutter.include_components }}:
    remove_dirs(
        'src/{{ cookiecutter.import_name }}/module',
        'src/{{ cookiecutter.import_name }}/widgets',
        'vue-components',
    )

if not {{ cookiecutter.include_app }}:
    remove_dirs(
        'src/{{ cookiecutter.import_name }}/app',
        'bundles',
        'examples',
    )

if not {{ cookiecutter.include_components_only }}:
    remove_dirs('src/trame')

if not {{ cookiecutter.include_ci }}:
    remove_dirs(
        '.github',
        'tests',
    )
    remove_files(
        'noxfile.py',
        '.prettierignore',
        '.codespellrc',
        '.commitlintrc.js',
        '.pre-commit-config.yaml',
    )
