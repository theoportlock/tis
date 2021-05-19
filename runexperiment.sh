#!/bin/bash -e
#name=$(basename $(ls Experiments/* | fzf))

name="parrot.py"
cp Experiments/$(basename $name .py)/$name . 
echo "$(date): $name begin"
timeout 50 python $name
echo "$(date): $name done"
