import numpy as np

def int_to_binarr(x,shape,on=1,off=0):
    arr = []
    while x > 0:
        if x % 2 == 0:
            arr.append(0)
        else:
            arr.append(1)
        x = int(x/2)
    while len(arr) < shape:
        arr.append(0)
    return np.array(arr)

def all_binarrs(shape,on=1,off=0):
    binarrs = []
    for i in range(2**shape):
        binarrs.append(int_to_binarr(i,shape,on,off))
    return binarrs

def all_directions(shape,on,off):
    zero = np.array([0.0 for i in range(shape)])
    arr  = []
    
    for i in range(shape):
        t = zero.copy()
        t[i] = on
        arr.append(t)

    for i in range(shape):
        t = zero.copy()
        t[i] = off
        arr.append(t)

    return arr

print(all_directions(6,0.2,-0.2))