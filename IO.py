def file2int(filename):
    # loads an integer from file
    with open(filename,'r') as of:
        return(int(of.read()[::-1],2))

def int2file(arr,filename):
    # saves an integer to file
    with open(filename,"w") as of:
        of.write(str(bin(arr)[:1:-1]))

def file2set(filename):
    # loads a set from file
    with open(filename,'r') as of:
        return(set([int(i[::-1],2) for i in of.read().splitlines()]))

def mem2set():
    import os.path
    if not os.path.isfile("memory"):
        set2file(set(), "memory")
    return file2set("memory")

def set2file(setnam,filename):
    # saves the set in a file
    with open(filename,"w") as of:
        for i in setnam:
            of.write(str(bin(i))[:1:-1]+"\n")

def text2arr(filename):
    # opens textfile as one integer
    with open(filename) as tf:
        return sum(list(map(int,''.join(format(ord(x),'b') for x in tf.read()))))

def powerset(items):
    # finds all combinations of list elements
    from itertools import compress, product
    return list(set(compress(items, mask)) for mask in product(*[[0,1]]*len(items)))[1:]

def convert(arr):
    # conversion to see only the active bits
    converted_input = []
    for i in range(arr.bit_length()):
        if 2**i & arr == 2**i:
            converted_input.append(2**i)
    return converted_input

