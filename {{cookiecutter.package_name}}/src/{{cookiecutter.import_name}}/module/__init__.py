from pathlib import Path

# Compute local path to serve
serve_path = str(Path(__file__).with_name("serve").resolve())

# Serve directory for JS/CSS files
serve = {"__{{cookiecutter.import_name}}": serve_path}

# List of JS files to load (usually from the serve path above)
scripts = ["__{{cookiecutter.import_name}}/{{cookiecutter.import_name}}.umd.js"]

# List of CSS files to load (usually from the serve path above)
# styles = ["__{{cookiecutter.import_name}}/style.css"]

# List of Vue plugins to install/load
vue_use = ["{{cookiecutter.import_name}}"]

# Uncomment to add entries to the shared state
# state = {}


# Optional if you want to execute custom initialization at module load
def setup(app, **kwargs):
    """Method called at initialization with possibly some custom keyword arguments"""
    pass
