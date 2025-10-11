#!/bin/bash
source env.sh

# Initialise
write.py -i 00000 -o work/input
write.py -i 00000 -o work/memory

for i in {1..100}; do
	rando.py -l 10 -s 0.7 -o work/action
	\cp work/action work/input
	merge.py -a work/input -b work/action -pa 10 -pb 10 -o work/c0
	memor.py -i work/c0 -m work/memory -o work/memory
	echo "This is loop number $i."
done

# results never go over 124 kb, regardless of number of loops
du -sh work/*

read.py -i work/input
read.py -i work/memory
read.py -i work/action
read.py -i work/c0

# How to subtract the self dataset connections?
# Do i need an additional step to add one to a supermemory file?
