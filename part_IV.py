# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 20:07:48 2016

@author: Sergey
"""
import numpy as np
import copy
def gradient(A,u,b):
    return A * u - b
    
import matplotlib.pyplot as plt   
    

def part4_1():
        
    dx = 0.1
    dt = 0.001
    Board = 10.0        
    imax = int(Board / (dx) - 1.0)
    x = np.linspace(-Board, Board, 2 * imax + 3)[1:-1]
    u = (1 / np.sqrt(2 * np.pi)) * np.matrix(np.exp(-x**2 / 2.0))
    u = u.T
    b = 1.0
    
    A = np.diag([1 + 2 * b *dt/(dx)**2 for i in range(2 * imax + 1)], 0)
    A = A + np.diag([-b * dt/(dx)**2 for i in range(2 * imax)], -1)
    A = A + np.diag([-b * dt/(dx)**2 for i in range(2 * imax)], 1)
    A = np.matrix(A)
    plt.plot(x, u, 's', linestyle = '-', color = 'r', markersize = 2);
    
    T = 10
    for i in range(int(T/dt)):
        u = np.array(u)
        B = np.matrix(A +  dt * np.diag((u**3).T[0,:], 0))#
        u = np.matrix(u)
        c = np.matrix(copy.copy(u))
                
                
        for k in xrange(20):
            grad = gradient(B, u, c)
            norm = np.linalg.norm(grad, 2)
            ro = norm**2/(grad.T * A * grad)
            u = u -  grad * ro

        if (i * dt in [1.0 * i for i in range(0,T,2)]):
            plt.plot(x, u, 's', linestyle = '-', color = 'r', markersize = 2);
            
    plt.plot(x, u, 's', linestyle = '-', color = 'r', markersize = 2);