@echo off

set PYTHON=
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS=--listen --enable-insecure-extension-access --medvram --opt-sub-quad-attention --disable-nan-check --no-half --theme dark --api --cors-allow-origins http://localhost:5173

call webui.bat
