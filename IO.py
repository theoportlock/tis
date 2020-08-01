def file2arr(filename):
    with open(filename,'r') as of:
        return(int(reversed(of.read()),2))

def arr2file(arr,filename):
    with open(filename,"w") as of:
        of.write(reversed(str(bin(arr))[2:]))

def file2set(filename):
    with open(filename,'r') as of:
        return(set([int(reversed(i),2) for i in of.read().splitlines()]))

def set2file(setnam,filename):
    with open(filename,"w") as of:
        for i in setnam:
            of.write(reversed(str(bin(i))[2:])+"\n")
