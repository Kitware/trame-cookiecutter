import os

# Compute local path to serve
serve_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "serve"))

# Serve directory for JS/CSS files
serve = {"__{{cookiecutter.name}}": serve_path}

# List of JS files to load (usually from the serve path above)
scripts = ["__{{cookiecutter.name}}/vue-{{cookiecutter.name}}.umd.min.js"]

# List of CSS files to load (usually from the serve path above)
styles = ["__{{cookiecutter.name}}/vue-{{cookiecutter.name}}.css"]

# List of Vue plugins to install/load
vue_use = ["{{cookiecutter.name}}"]

# Uncomment to add vuetify config
# vuetify = {} 

# Uncomment to add entries to the shared state
# state = {}

# Optional if you want to execute custom initialization at module load
def setup(**kwargs):
    """Method called at initialization with possibly some custom keyword arguments"""
    pass