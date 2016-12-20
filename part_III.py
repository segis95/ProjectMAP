# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 16:29:04 2016

@author: Sergey
"""

import numpy as np

def expon(x, x0, sigma):
    return np.exp(-0.5 * (x - x0)**2/sigma**2)

def grad_i(alpha1, alpha2, sigma1, sigma2, x01, x02, x):
    L = [0 for i in range(6)]
    L[0] =  -expon(x, x01, sigma1)
    L[1] =  -expon(x, x02, sigma2)
    L[2] =  -alpha1 * (x - x01)**2/sigma1**3.0 * expon(x, x01, sigma1)
    L[3] =  -alpha2 * (x - x02)**2/sigma2**3 * expon(x, x02, sigma2)
    L[4] = alpha1 * (x01 - x)/sigma1**2 * expon(x, x01, sigma1)
    L[5] = alpha2 * (x02 - x)/sigma2**2 * expon(x, x02, sigma2)
    
    return L
    
def Df(alpha1, alpha2, sigma1, sigma2, x01, x02, x):
    L = [0 for i in range(len(x))]
    for i in range(len(x)):
        L[i] = grad_i(alpha1, alpha2, sigma1, sigma2, x01, x02, x[i])
    
    return np.matrix(L)
    
    
def g(alpha1, alpha2, sigma1, sigma2, x01, x02, x):
    return alpha1 * expon(x, x01, sigma1) + alpha2 * expon(x, x02, sigma2)
    
def f(alpha1, alpha2, sigma1, sigma2, x01, x02, x, y):
    L = [0 for i in range(8)]
    
    for i in range(8):
        L[i] = [y[i] - g(alpha1, alpha2, sigma1, sigma2, x01, x02, x[i])]
        
    return np.matrix(L)
    
    
    
    
def part_3():
        
    alpha1 = 1.0
    alpha2 = 1.0
    sigma1 = 1.0
    sigma2 = 1.0
    x01 = 3.0
    x02 = 6.0
    
    beta = np.matrix([[alpha1],[alpha2],[sigma1],[sigma2],[x01],[x02]])
    
    x = [1.0 * i for i in range(1,9)]
    y = [0.127, 0.2, 0.3, 0.25, 0.32, 0.5, 0.7, 0.9]
    
    norm = 1.0
    
    while(norm > 1e-2):
        
        DF = Df(beta[0,0], beta[1,0], beta[2,0], beta[3,0], beta[4,0], beta[5,0], x)
        fun = f(beta[0,0], beta[1,0], beta[2,0], beta[3,0], beta[4,0], beta[5,0], x, y) 
        beta = beta - (DF.T * DF).I * DF.T * fun
        norm = np.linalg.norm(DF.T * fun, 2)
        print(norm, 0.5 * np.linalg.norm(fun, 2))
    
        
    
    
    
    
    
    
    
    
    
    
    
    