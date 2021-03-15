#!/bin/bash -e
#name=$(basename $(ls Experiments/* | fzf))

name="parrot.py"
timelim=50

result_dir="Experiments/$(basename $name .py)/results"
result="$(date +"%T").csv"

mkdir -p $result_dir

trap "[ ! -e $name ] || rm $name " EXIT
cp Experiments/$(basename $name .py)/$name . 

timeout $timelim python $name > $result_dir/$result

#mprof -o $results
