@echo off
setlocal
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" goto run
where uv >nul 2>nul
if errorlevel 1 (
  echo Paigalda esmalt uv: https://docs.astral.sh/uv/getting-started/installation/
  pause
  exit /b 1
)
set "UV_CACHE_DIR=%CD%\.cache\uv"
set "UV_PYTHON_INSTALL_DIR=%CD%\.python-runtime"
uv sync --python 3.13 --frozen
if errorlevel 1 (
  pause
  exit /b 1
)
:run
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
