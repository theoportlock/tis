export PATH=$PATH:../src/
write.py 10011 -o ../data/input
write.py 0 -o ../data/memory
memorize.py
read.py
read.py -f ../data/memory

write.py 10111 -o ../data/input
memorize.py
read.py
read.py -f ../data/memory
