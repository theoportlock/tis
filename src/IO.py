import os.path

# write a new set/int/txt to file before reading if one doesnt exist

def intfile(obj=0, mode='in', filename=''):
    if mode == "in":
        # write a new integer to file before reading if one doesnt exist
        if not os.path.isfile(filename):
            with open(filename, "w") as of:
                of.write(str(bin(1)[:1:-1]))
        with open(filename, 'r') as of:
            return (int(of.read()[::-1],2))
    elif mode == "out":
        with open(filename, "w") as of:
            of.write(str(bin(obj)[:1:-1]))


def setfile(obj={}, mode='in', filename=''):
    if mode == "in":
        if not os.path.isfile(filename):
            with open(filename, "w") as of:
                for i in obj:
                    of.write(str(bin(i))[:1:-1]+"\n")
        with open(filename, 'r') as of:
            return(set([int(i[::-1],2) for i in of.read().splitlines()]))
    elif mode == "out":
        with open(filename, "w") as of:
            for i in obj:
                of.write(str(bin(i))[:1:-1]+"\n")


def txtfile(obj=0, mode='in', filename=''):
    if mode == "in":
        # write a new textfile to file before reading if one doesnt exist
        if not os.path.isfile(filename):
            with open(filename, "wb") as of:
                of.write(obj.to_bytes((obj.bit_length() + 7) // 8, 'big') or b'\0')
        with open(filename, "rb") as of:
            return int.from_bytes(of.read(), byteorder="big")
    elif mode == "out":
        with open(filename, "wb") as of:
            of.write(obj.to_bytes((obj.bit_length() + 7) // 8, 'big') or b'\0')
