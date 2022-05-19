from {{cookiecutter.import_name}}.widgets.{{cookiecutter.import_name}} import *


def initialize(server):
    from {{cookiecutter.import_name}} import module

    server.enable_module(module)
