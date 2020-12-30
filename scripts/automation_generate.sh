#!/bin/bash

VIRTUAL_ENV=$(pwd)/../venv-sdk
export VIRTUAL_ENV
PATH="$VIRTUAL_ENV/bin:$PATH"
export PATH


# generate code and package
python -m packaging_tools.auto_codegen "$1" "../venv-sdk/auto_temp.json" 2>&1
echo "[Generate] codegen done!!!"
python -m packaging_tools.auto_package "../venv-sdk/auto_temp.json" "$2" 2>&1
echo "[Generate] generate done!!!"
