#!/bin/bash

echo "This little script will setup the environment..."

echo "Installing python3 external utilities [ pip, python3-venv ]"
sudo apt install python3-pip python3-venv

echo "Seting up virtual environment..."
python3 -m venv sandbox

echo "First installation of packages..."
source sandbox/bin/activate
pip install --upgrade pip
pip install click python-dotenv

pip install --editable tools/khabuild

deactivate

echo "Finished! Starting shell..."
source khaos.sh