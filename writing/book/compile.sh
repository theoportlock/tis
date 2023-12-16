#!/bin/bash
pdflatex -shell-escape main.tex &&
makeindex -s main.ist -t main.glg -o main.gls main.glo &&
bibtex main && 
pdflatex -shell-escape main.tex &&
pdflatex -shell-escape main.tex
