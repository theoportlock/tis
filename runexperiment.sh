#!/bin/bash -e
name=$(find experiments/*/*.py -type f | sed 's|.*/.*/||g' | fzf)
bname=$(basename -s .py $name)
timelim=60
result_dir="experiments/$bname/results"
result="$(date +"%T").tsv"

echo "saving to $result_dir/$result"

mkdir -p $result_dir

trap "[ ! -e $name ] || rm $name " EXIT
cp experiments/$bname/$name . 
echo "$(date): $name begin"

timeout $timelim python $name | tee $result_dir/$result
echo "$(date): $name done"

#timeout $timelim python -c 'print("testing")' > test.txt
#mprof -o $results
