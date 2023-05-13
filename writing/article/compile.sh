#!/bin/bash
fullnam="*.tex"
nam=$(echo $fullnam | cut -f 1 -d  '.')
pdflatex -shell-escape $fullnam && 
makeindex -s $nam.ist -t $nam.glg -o $nam.gls $nam.glo &&
bibtex $nam && 
pdflatex -shell-escape $fullnam && 
pdflatex -shell-escape $fullnam &
