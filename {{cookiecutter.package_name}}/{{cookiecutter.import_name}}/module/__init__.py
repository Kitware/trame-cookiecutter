from pathlib import Path

# Compute local path to serve
serve_path = str(Path(__file__).with_name("serve").resolve())

# Serve directory for JS/CSS files
serve = {"__{{cookiecutter.import_name}}": serve_path}

# List of JS files to load (usually from the serve path above)
scripts = ["__{{cookiecutter.import_name}}/vue-{{cookiecutter.import_name}}.umd.min.js"]

# List of CSS files to load (usually from the serve path above)
styles = ["__{{cookiecutter.import_name}}/vue-{{cookiecutter.import_name}}.css"]

vuetify_config = {}

# List of Vue plugins to install/load
vue_use = ["{{cookiecutter.import_name}}", ("trame_vuetify", vuetify_config)]

# Uncomment to add entries to the shared state
# state = {}

# Optional if you want to execute custom initialization at module load
def setup(app, **kwargs):
    """Method called at initialization with possibly some custom keyword arguments"""
    pass
