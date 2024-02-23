'''
import src.functions as f
load src/functions.py
'''

def comb(integer):
    converted = [2**(i-1) for i in uncomb(integer)]
    out=[]
    for i in range(1, 2**len(converted)):
        out.append(sum([converted[j-1] for j in uncomb(i)]))
    return sum([2**(i-1) for i in out])

def uncomb(arr: int) -> list:
    converted_input = []
    for i in range(arr.bit_length()):
        if 2**i & arr == 2**i:
            converted_input.append(i+1)
    return converted_input

def int2bin(integer):
    if integer:
        return bin(integer)[:1:-1]
    else:
        return ""

def bin2int(binary):
    if binary: 
        return int(binary[::-1],2)
    else:
        return 0

def paircomb(int1, int2):
    out = 0
    for i in uncomb(comb(int1)):
        for j in uncomb(comb(int2)):
            out+=2**(i+j-1)
    return out

def newpaircomb(int1, int2):
    return int1*int2*2

#a = np.random.randint(1, 24, size=(10, 2))
#for i in a:
    #print(paircomb(int(i[0]), int(i[1])), newpaircomb(int(i[0]), int(i[1])))
