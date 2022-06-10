#!/usr/bin/env bash

now="Commit version $(date)"

git add .
git commit -m "$now"

git push origin main

exit N
