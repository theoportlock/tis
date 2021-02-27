#!/bin/bash
name=$(basename $(ls experiment/* | fzf))
cp experiment/$name . &&
python $name
rm $name
