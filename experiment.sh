#!/bin/bash
name=$(basename $(ls experiments/* | fzf))
cp experiments/$name . &&
python $name
rm $name
