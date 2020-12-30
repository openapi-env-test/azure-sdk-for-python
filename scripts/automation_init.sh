#!/bin/bash

rm -rf ../venv-sdk
python3 -m venv ../venv-sdk
VIRTUAL_ENV=$(pwd)/../venv-sdk
export VIRTUAL_ENV
PATH="$VIRTUAL_ENV/bin:$PATH"
export PATH
python scripts/dev_setup.py -p azure-core
echo "{}" >> $2

# node version degrade
sudo npm install -g n
sudo n 10.15.0
export PATH=/usr/local/n/versions/node/10.15.0/bin:$PATH
node -v

echo "[Generate] init success!!!"
