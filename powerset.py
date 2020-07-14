from itertools import compress, product

def a(items):
    return( set(compress(items,mask)) for mask in product(*[[0,1]]*len(items)))
