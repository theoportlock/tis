#!/bin/bash -e
#name=$(basename $(ls Experiments/* | fzf))

name="parrot.py"
timelim=360

result_dir="Experiments/$(basename $name .py)/results"
result="$(date +"%T").csv"

echo "saving to $result_dir/$result"

mkdir -p $result_dir

trap "[ ! -e $name ] || rm $name " EXIT
cp Experiments/$(basename $name .py)/$name . 
echo "$(date): $name begin"
timeout $timelim python $name > $result_dir/$result
echo "$(date): $name done"

#timeout $timelim python -c 'print("testing")' > test.txt

#mprof -o $results
