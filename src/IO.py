def intfile2int(filename):
    # loads an integer from file
    with open(filename, 'r') as of:
        return(int(of.read()[::-1],2))

def int2intfile(arr, filename):
    # saves an integer to file
    with open(filename, "w") as of:
        of.write(str(bin(arr)[:1:-1]))

def intfile2set(filename):
    # loads a set from file
    with open(filename, 'r') as of:
        return(set([int(i[::-1],2) for i in of.read().splitlines()]))

def mem2set(filename):
    import os.path
    if not os.path.isfile(filename):
        set2intfile(set(), filename)
    return intfile2set(filename)

def textpre2int(filename):
    import os.path
    if not os.path.isfile(filename):
        int2textfile(1, filename)
    return textfile2int(filename)

def intpre2int(filename):
    import os.path
    if not os.path.isfile(filename):
        int2intfile(1, filename)
    return intfile2int(filename)

def set2intfile(setnam, filename):
    # saves the set in a file
    with open(filename, "w") as of:
        for i in setnam:
            of.write(str(bin(i))[:1:-1]+"\n")

def textfile2int(filename):
    # opens textfile as one integer
    with open(filename, "rb") as tf:
        return int.from_bytes(tf.read(), byteorder="big")

def int2textfile(arr, filename):
    # saves the integer as a text to file
    with open(filename, "wb") as tf:
        #print(bytearray(arr))
        tf.write(arr.to_bytes((arr.bit_length() + 7) // 8, 'big') or b'\0')

