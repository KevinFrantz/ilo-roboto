#!/bin/bash
echo "Allgemeine Setups werden ausgefuehet..."
pacman -Syyu
echo "Python spezifische Installationen werden ausgefuehrt"
pacman -S python python-pip python3-pip
pip install --upgrade pip
pip install nanpy

