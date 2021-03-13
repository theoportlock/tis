#!/bin/bash -e
#name=$(basename $(ls Experiments/* | fzf))

name="parrot.py"
timelim=50

results="Experiments/$(basename $name .py)/results"
mkdir -p $results

trap "[ ! -e $name ] || rm $name " EXIT
cp Experiments/$(basename $name .py)/$name . 

#timeout $timelim \
#	mprof -o $results \
#		python $name \
#			> $results.log

timeout $timelim \
	python $name \
		> $results.log
