#!/usr/bin/env bash

echo 'Enter the commit message'
read commitMessage

now="$(date)"

git add .
git commit -m "$now"

git push origin main

exit N
