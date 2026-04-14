python -m PyInstaller ^
  --hidden-import pkgutil ^
  --windowed ^
  --collect-data trame_vuetify ^
  --collect-data trame_vtk ^
  --collect-data trame_client ^
{%- if cookiecutter.include_components %}
  --collect-data {{cookiecutter.package_name}} ^
{%- endif %}
  .\run.py
