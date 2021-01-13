#!/bin/bash

rm -rf $(TMP_FOLDER)/venv-sdk
python3 -m venv $(TMP_FOLDER)/venv-sdk
VIRTUAL_ENV=$(TMP_FOLDER)/venv-sdk
export VIRTUAL_ENV
PATH="$VIRTUAL_ENV/bin:$PATH"
export PATH
python scripts/dev_setup.py -p azure-core
echo "{}" >> $2
echo "[Generate] init success!!!"
