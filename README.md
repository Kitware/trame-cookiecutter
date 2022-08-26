# Cookiecutter Trame

This is a [Cookiecutter](https://github.com/audreyr/cookiecutter) template that generates
[Trame](https://github.com/kitware/trame) boilerplate.

## Quick Start

Install the Cookiecutter package:

```bash
pip install cookiecutter
```

## Trame v1

```bash
cookiecutter gh:kitware/trame-cookiecutter -c v1
```

## Trame v2

```bash
cookiecutter gh:kitware/trame-cookiecutter
```

## What do you get?

This project contains a Cookiecutter template that helps you create new
Python 3.6+ package for trame by automatically generating most of the boiler
plate content for you.

The cookiecutter will ask you set of questions to refine what you aim to build
using trame, but the most important one which will affect the shape of what you
will get is the **project_type**.

The **project_type** can be only one of the following options:

* **App**
    This will provide the infrastructure for building a trame application that
    can leverage all the existing set of trame components using only Python.
    By default a simple vtk.js application is used as reference to provide
    the trame basic while demonstrating an interactive application with code
    separation between the Python core and the web frontend.
    Whithin that Python package, a jupyter helper module will also be available
    to run and show your application within a jupyter environment.
    On top of that Python package, you will have access to several bundling
    option ranging from a standalone executable to a docker image for cloud
    deployment.
* **App with Components**
    This will provide the same infrastructure as above but with an additional
    directory that will contain a vue.js project for defining new UI elements
    that can then be used within your trame application. This path is more
    advanced than the plain Application one as it will require some Web
    development knowledge.
    Also on top of that new web structure, a Python module is getting created
    to bridge what has been defined on the JavaScript side so it can be used
    at the Python level.
* **Components**
    This is the same thing as above but without the application part.
    Basically it creates the Python package so it can be pip installable
    and used by any trame application at the Python level.
    But as before stated, this will require some Web development knowledge.


The structure produced by this Cookiecutter template contains the following items:

```
.
├── .*                         # (Continuous integration option) Python quality control + Github actions
├── CONTRIBUTING.rst           # Minimal content for project contribution
├── LICENSE                    # Selected license
├── MANIFEST.in                # List external files/directories that needs to be part of the Python package
├── README.rst                 # Minimal README using RST format so it get exposed to PyPI if deployed
├── bundles                    # (App option) Bundling helper for Application
│   ├── desktop                  # How to create a desktop executable
│   │   ├── macOS/*                # On macOS
│   │   └── windows/*              # On Windows
│   └── docker/*                 # How to create docker image for cloud service deployment
├── examples                   # (App option) Usage example of your application
│   └── jupyter                  # Inside a Jupyter notebook
├── setup.cfg                  # Configuration file for your Python package
├── setup.py                   # Python package entry point
├── tests/*                    # Testing infrastructure
├── f"{import_name}"           # Root directory for your Python package
│   ├── app                      # (App option) Root directory for your application
│   │   ├── engine.py              # Core Python code for your application
│   │   ├── jupyter.py             # Built-in adapter for usage in Jupyter
│   │   ├── main.py                # Main executable setting-up your engine+ui
│   │   └── ui.py                  # UI definition and bridge to Web frontend
│   ├── module/*                 # (Component option) web files and configuration
│   └── widgets/*                # (Component option) web to Python mapping
├── trame/*                      # (Component only option) adapter to streamline import and usage for trame
└── vue-components/*             # (Component option) Standard Vue.js project for creating a Vue plugin
```

### Configuration options

* project_name [Trame App]: Human readable name for your application
* project_type [App]: Project type described in more detail above
* author            : Used for your package definition (setup.cfg)
* short_description : Used for your package definition (setup.cfg)
* license [BSD]     : Used for your package definition (setup.cfg+LICENSE)
* include_continuous_integration: Create Github actions with Python quality control validation
* package_name      : Application name to use for `pip install` or application execution
* import_name       : Physical name of the root directory of your application/library
