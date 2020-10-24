#!/bin/bash
cp $1 ../ &&
cd ../ &&
python $1;
rm $1;
cd experiments
