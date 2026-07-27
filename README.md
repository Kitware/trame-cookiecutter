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
Python 3.10+ package for trame by automatically generating most of the boiler
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
    Within that Python package, a jupyter helper module will also be available
    to run and show your application within a jupyter environment.  On top of
    that Python package, you will have access to several bundling option ranging
    from a standalone executable to a docker image for cloud deployment.
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
│   └── jupyter/*                # Notebook to use inside Jupyter
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

* **project_name [Trame App]:** Human readable name for your application
* **project_type [App]:** Project type described in more detail above
* **author:** Used for your package definition (setup.cfg)
* **short_description:** Used for your package definition (setup.cfg)
* **license [BSD]:** Used for your package definition (setup.cfg + LICENSE)
* **include_continuous_integration:** Create Github actions with Python quality control validation (.*)
* **package_name:** Application name to use for `pip install` or application execution
* **import_name:** Physical name of the root directory of your application/library

### Usage example

__Caution__: If you don't keep the same options, please look at the generated README to properly capture the specificity of your setup.

```bash
$ python3 -m venv .venv
$ source ./.venv/bin/activate
$ python -m pip install --upgrade pip
$ pip install cookiecutter

$ cookiecutter gh:kitware/trame-cookiecutter

    project_name [Trame App]: Visualis
    Select project_type:
    1 - App
    2 - App with Components
    3 - Components
    Choose from 1, 2, 3 [1]:
    author [Trame Developer]: Kitware Inc.
    short_description [An example Trame application]: VTK viewer for 3d stuff
    Select license:
    1 - BSD License
    2 - MIT License
    3 - ISC License (ISCL)
    4 - Apache Software License
    5 - GNU General Public License v3 (GPLv3)
    6 - Other
    Choose from 1, 2, 3, 4, 5, 6 [1]: 4
    include_continuous_integration [y]: n
    package_name [visualis]:
    import_name [visualis]:

cd visualis
pip install . # Install your new application

pip install pywebview  # For app usage
pip install jupyterlab # For Jupyter usage
```

Then you can run it using your browser with the following command line:

```bash
visualis
```

![Standard execution with auto browser open](https://github.com/Kitware/trame-cookiecutter/blob/master/docs/browser.jpg?raw=true)

Or show it as a desktop application with the following command line:

```bash
visualis --app
```

![Desktop Application mode](https://github.com/Kitware/trame-cookiecutter/blob/master/docs/app.jpg?raw=true)

Or with Jupyter

```bash
jupyter-lab
```

![Jupyter Notebook Example](https://github.com/Kitware/trame-cookiecutter/blob/master/docs/jupyter.jpg?raw=true)

And if you have docker

```bash
cd bundles/docker
./scripts/build_image.sh
./scripts/run_image.sh
#> open http://localhost:8080/
```

## Publishing the widget or application

In order to publish your repository and make it available to the community, here is the publish
process checklist.

- [ ] Clean the repository
- [ ] Publish to [PyPI](https://pypi.org/)
- [ ] Publish to [conda-forge](https://conda-forge.org/)
- [ ] Add to the [trame widgets catalog](https://kitware.github.io/trame/guide/intro/widgets.html)
or [trame applications catalog](https://kitware.github.io/trame/guide/intro/applications.html)
- [ ] Make a post on the [trame news page](https://kitware.github.io/trame/news.html)
- [ ] Make a github discussion in the
[Announcements category](https://github.com/Kitware/trame/discussions/categories/announcements)

### Clean the repository

To encourage contribution and usage make sure the code is clean, create examples and tests, have a clear README with screenshots.

#### GitHub repository

- [ ] Have a preview image in your repository github page, Settings > General > Social preview. The
image should be at least 640×320px, have 2:1 ratio and 40px padding (rendering might put borders).
- [ ] Have your About section (from your repository page) such that
    - [ ] The description is comprehensive 
    - [ ] You use topics `trame`, `trame-widget` or `trame-app`, `vue2`, `vue3`, `vtk`, `paraview`,
    `3d-slicer*` if related to those. If actively maintained by Kitware, use the
    `trame-maintenance-program` topic.

### Publish to PyPI

First you need to register to PyPI, go to [Publishing](https://pypi.org/manage/account/publishing/) and add a pending publisher for your repository.

This cookiecutter already provides a GitHub workflow that publishes to PyPI on each new version.
Follow the instruction from [the PyPI
documentation](https://docs.pypi.org/trusted-publishers/using-a-publisher/) if GitHub Actions aren't
available.

### Publish to conda-forge

Follow the instruction from the [conda-forge
documentation](https://conda-forge.org/docs/maintainer/adding_pkgs/). If the repository is published
to PyPI first, publishing to conda-forge is easier.

### Add your widget/application to the trame catalogs

Make a PR on the [trame repository](https://github.com/Kitware/trame) to add an entry to
[docs/vitepress/external_repos.yml](https://github.com/Kitware/trame/blob/master/docs/vitepress/external_repos.yml).

#### GitHub-hosted repository

```yml
# ... other repositories

https://github.com/your-username/repo-name: {}
```

All the information will be fetched from GitHub.

#### Non GitHub-hosted repository

Add information manually, it won't update automatically.

```yml
# ... other repositories

your-repository-url:
  topics: [trame, ...] # Follow the rules for topics in GitHub
  name:                # Your repository name
  description:         # Comprehensive description of your repository
  image:               # URL of a preview image for your repository
  stars:               # Number of stars
  createdAt:           # Date of creation in the YYYY-MM-DDT00:00:00Z format
  commitCount:         # Number of commits
  pullRequestCount:    # Number of pull requests
  lastCommitDate:      # Date of the last commit in the YYYY-MM-DDT00:00:00Z format
  lastTimeSeen:        # Today date in the YYYY-MM--DDT00:00:00Z format
  trusted:             # true only if the repository is owned by Kitware
```

### Post on the trame news page

Make a PR on the [trame repository](https://github.com/Kitware/trame) to add an entry to
[docs/vitepress/news.md](https://github.com/Kitware/trame/blob/master/docs/vitepress/news.md) in the following format.
```md
## Month DD, YYYY

Short description of the widget with a link to your repository.

...Other news post...
```

### Post on the trame GitHub discussions

Make a short post on [announcements category](https://github.com/Kitware/trame/discussions/categories/announcements) of the trame repository's discussions.
