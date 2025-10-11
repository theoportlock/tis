#!/bin/bash
source env.sh

write.py -i 10011 -o work/input
write.py -i 0 -o work/memory

memorize.py -i work/input -m work/memory -o work/memory1

read.py -i work/input
read.py -i work/memory
read.py -i work/memory1
