#!/bin/bash -e
name=$(find experiments/*/code/*.py -type f | sed 's|.*/.*/||g' | fzf)
bname=$(basename -s .py $name)
timelim=60
result_dir="experiments/$bname/results"
result="$(date +"%T").tsv"

echo "saving to $result_dir/$result"

mkdir -p $result_dir

trap "[ ! -e $name ] || rm $name " EXIT
ln -s experiments/$bname/code/$name . 
echo "$(date): $name begin"

timeout $timelim python -u $name | tee $result_dir/$result
echo "$(date): $name done"

#timeout $timelim python -c 'print("testing")' > test.txt
#mprof -o $results
