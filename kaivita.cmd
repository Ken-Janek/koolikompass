@echo off
rem Hoia muutujad selle skripti piires ja vali projekti kaust.
setlocal
cd /d "%~dp0"
rem Olemasoleva virtuaalkeskkonnaga saab seadistuse vahele jatta.
if exist ".venv\Scripts\python.exe" goto run
where uv >nul 2>nul
if errorlevel 1 (
  echo Paigalda esmalt uv: https://docs.astral.sh/uv/getting-started/installation/
  pause
  exit /b 1
)
set "UV_CACHE_DIR=%CD%\.cache\uv"
set "UV_PYTHON_INSTALL_DIR=%CD%\.python-runtime"
rem Paigalda lukustatud soltuvused ja vajaduse korral Python.
uv sync --python 3.13 --frozen
if errorlevel 1 (
  pause
  exit /b 1
)
:run
rem Uuenda andmebaasi skeemi enne kohaliku arendusserveri kaivitamist.
set "DJANGO_DEBUG=1"
".venv\Scripts\python.exe" app/manage.py migrate
if errorlevel 1 (
  pause
  exit /b 1
)
echo.
echo Ava brauseris: http://127.0.0.1:8000
echo Peatamiseks vajuta Ctrl+C.
echo.
".venv\Scripts\python.exe" app/manage.py runserver 127.0.0.1:8000
pause
