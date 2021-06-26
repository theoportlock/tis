#!/bin/bash -e
#name=$(basename $(ls experiments/* | fzf))

name="parrot.py"
timelim=360

result_dir="experiments/$(basename $name .py)/results"
result="$(date +"%T").csv"

echo "saving to $result_dir/$result"

mkdir -p $result_dir

trap "[ ! -e $name ] || rm $name " EXIT
cp experiments/$(basename $name .py)/$name . 

timeout $timelim python $name > $result_dir/$result

#timeout $timelim python -c 'print("testing")' > test.txt
#mprof -o $results
