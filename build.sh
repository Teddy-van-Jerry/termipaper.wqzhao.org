#!/bin/sh

python ./generate.py
mkdir -p build
cp -r ./lists ./build
cp index.html ./build
cp style.css ./build
