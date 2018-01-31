#!/bin/bash
cd ./Documents/zhaonisuanzhang;
git pull
python3 suanzhang.py;
git add .
git commit -m "zhao"
git push
