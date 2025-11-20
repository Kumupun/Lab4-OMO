import numpy as np

def roots_for(L,domain):
    res = L.roots() 
    res_real = res[np.isreal(res)].real
    return res_real

def roots_back(L):
    res = L(0)
    if res==None:
        print("The resulting inverse polynomial has no roots.")
    return res
    