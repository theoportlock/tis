def file2arr(fil):
    import numpy as np
    with open(fil,'r') as tf:
        return(int(tf.read(),2))

def arr2file(arr,nam):
    import numpy as np
    with open(nam,"w") as of:
        of.write(str(bin(arr))[2:-1])
