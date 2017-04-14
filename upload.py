#!/bin/sh

git init
git add .
git config --global user.name "Tyler"
git config --global user.email "tylerschmidt@nevada.unr.edu"
git commit -m "First commit"
git remote add origin https://github.com/tz7/sensor.git
git push origin master
