pyinstaller ^
  --hidden-import vtkmodules.all ^
  --collect-data pywebvue ^
  --onefile ^
  --windowed ^
  --icon {{cookiecutter.package_name}}.ico ^
  .\run.py
