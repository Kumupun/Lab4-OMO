import numpy as np
import math

def Lagrange(x, given_coef, domain):
    coef = x.copy()
    n = len(coef) # number of nodes
    f = np.polynomial.Polynomial(given_coef)         #2*x**7 +3*x**6 +3*x**4 -3
    fn = f.deriv(n)
    L= np.polynomial.Polynomial([0])    
    for i in range(n):
        term = np.polynomial.Polynomial([1])
        for j in range(n):
            if j != i:
                term *= np.polynomial.Polynomial([-coef[j], 1]) / (coef[i] - coef[j])
        L += f(coef[i]) * term # f(coef[i]) - значення в вузлі y
    
    xx = np.linspace(domain[0], domain[1], 2000) # звичайний перебір для знаходження максимуму
    M = max(abs(fn(xx)))
    R = (M / math.factorial(n))*((domain[1] - domain[0])**(n) / 2**(2*n-1))
    return L, R

def Lagrange_inv(x, given_coef):
    coef = x.copy()
    n = len(x)
    f = np.polynomial.Polynomial(given_coef)  
    L_inv = np.polynomial.Polynomial([0])

    for i in range(n):
        yi = f(coef[i])
        Li = np.polynomial.Polynomial([1])
        for j in range(n):
            if i != j:
                Li *= np.polynomial.Polynomial([-f(coef[j]), 1]) / (yi - f(coef[j]))

        L_inv += x[i] * Li

    return L_inv