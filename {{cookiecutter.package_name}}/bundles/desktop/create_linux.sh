#!/bin/bash

python -m PyInstaller \
    --clean --noconfirm \
    --onefile \
    --hidden-import pkgutil \
    --collect-data trame_vuetify \
    --collect-data trame_vtk \
    ./run.py
