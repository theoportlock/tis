#!/bin/bash
#name=$(basename $(ls experiment/* | fzf))

name="parrot.py"
cp experiment/$name . 
echo "$(date): $name begin"
timeout 5000 python $name
