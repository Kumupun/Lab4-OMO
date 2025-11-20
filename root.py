import numpy as np

def roots_for(L,domain):
    res = np.roots(L.coef)

    res_in = [r for r in res if domain[0] <= r <= domain[1]]
    if len(res_in) == 0 :
        return None
    return res

def roots_back(L):
    res = L(0)
    if res==None:
        print("The resulting inverse polynomial has no roots.")
    return res
    