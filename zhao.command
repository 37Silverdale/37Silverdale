#!/bin/bash
cd ./Applications/37Silverdale
git pull
python3 suanzhang.py
git add .
git commit -m "zhao"
git push
