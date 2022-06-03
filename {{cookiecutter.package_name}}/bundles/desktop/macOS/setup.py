from setuptools import setup

ENTRY_POINT = ["{{cookiecutter.entry_point}}"]
DATA_FILES = []

OPTIONS = {
    "argv_emulation": False,
    "strip": True,
    "iconfile": "{{cookiecutter.package_name}}.icns",
    "includes": ["WebKit", "Foundation", "setuptools"],
}

setup(
    app=ENTRY_POINT,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
