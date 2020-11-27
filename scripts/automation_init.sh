#!/bin/bash

set - x
set - e
rm -rf ../venv-sdk
python3 -m venv ../venv-sdk
source ../venv-sdk/bin/activate
python scripts/dev_setup.py -p azure-core
python << EOF
echo "{}" >> $2
