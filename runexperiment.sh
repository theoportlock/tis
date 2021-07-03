#!/bin/bash -e
name=$(basename $(ls experiments/* | fzf))

timelim=60

result_dir="experiments/$(basename $name .py)/results"
result="$(date +"%T").tsv"

echo "saving to $result_dir/$result"

mkdir -p $result_dir

trap "[ ! -e $name ] || rm $name " EXIT
cp experiments/$(basename $name .py)/$name . 
echo "$(date): $name begin"

timeout $timelim python3.9 $name > $result_dir/$result
echo "$(date): $name done"

#timeout $timelim python -c 'print("testing")' > test.txt
#mprof -o $results
