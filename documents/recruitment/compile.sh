#!/bin/bash
fullnam="recruitment.tex"
nam=$(echo $fullnam | cut -f 1 -d  '.')
pdflatex -shell-escape $fullnam && 
pdflatex -shell-escape $fullnam &
