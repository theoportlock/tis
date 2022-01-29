#!/bin/bash -e
name=$(basename $(ls experiments/*/code/*.py | fzf))
bname=$(basename -s .py $name)
timelim=60
result_dir="experiments/$bname/results"
result="$(date +"%T").tsv"

echo "saving to $result_dir/$result"

mkdir -p $result_dir

trap "[ ! -e $name ] || rm $name " EXIT
ln experiments/$bname/code/$name . 
echo "$(date): $name begin"

timeout $timelim python $name | tee $result_dir/$result
echo "$(date): $name done"

#timeout $timelim python -c 'print("testing")' > test.txt
#mprof -o $results
