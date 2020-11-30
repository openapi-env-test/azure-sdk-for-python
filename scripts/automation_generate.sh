#!/bin/bash

VIRTUAL_ENV=$(pwd)/../venv-sdk
export VIRTUAL_ENV
PATH="$VIRTUAL_ENV/bin:$PATH"
export PATH
python -m packaging_tools.generate_script_v2 $1 $2
echo "[Generate] generate success!!!"
