#!/usr/bin/env python

from pathlib import Path
import shutil

PROJECT_DIRECTORY = Path.cwd()


def remove_file(filepath):
    Path(filepath).unlink()


def remove_dir(filepath):
    shutil.rmtree(filepath)


if not {{ cookiecutter.is_known_license }}:
    remove_file('LICENSE')

if not {{ cookiecutter.include_components }}:
    remove_dir('{{ cookiecutter.import_name }}/module')
    remove_dir('{{ cookiecutter.import_name }}/widgets')
    remove_dir('vue-components')
    remove_file('MANIFEST.in')

if not {{ cookiecutter.include_app }}:
    remove_dir('{{ cookiecutter.import_name }}/app')
    remove_dir('bundles')
    remove_dir('examples')
