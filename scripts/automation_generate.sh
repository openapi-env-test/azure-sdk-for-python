#!/usr/bin/env bash

source ../venv-sdk/Scripts/activate
python -m packaging_tools.generate_script_v2 $1 $2
echo "[Generate] generate success!!!"
