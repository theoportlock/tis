export PATH=$PATH:../src/
write.py 10011 -o ../data/input
write.py 0 -o ../data/memory
memorize.py
read.py -f ../data/memory
read.py
