def file2arr(filename):
    with open(filename,'r') as of:
        return(int(of.read(),2))

def arr2file(arr,filename):
    with open(filename,"w") as of:
        of.write(str(bin(arr))[2:-1])

def file2set(filename):
    with open(filename,'r') as of:
        return(set([int(i,2) for i in of.read().splitlines()]))

def set2file(setnam,filename):
    with open(filename,"w") as of:
        for i in setnam:
            of.write(str(bin(i))[2:]+"\n")
