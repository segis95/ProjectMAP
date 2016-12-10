# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 18:28:15 2016

@author: Sergey
"""
import numpy as np
import matplotlib.pyplot as plt


def gradient(A,u,b):
    return A*u - b
    
def gradient_Ros(x,y):
    return ( (2 * (x - 1) + 400 * (x**3 - x * y)) , (200 * (y - x**2)) )    
    
def Ros(x,y):
    return (x - 1.0)**2 + 100.0 * (x**2 - y)**2
    
def question_I_2_3(lambd):
    
    A = np.matrix([[1, 0], [0, lambd]])
    b = np.matrix([[1], [1]])
    
    L = [i for i in xrange(20)]
    
    plt.yscale('log')
    plt.title('log(|r_k|/|r_0|)')
    plt.xlabel('k')     
    
    for i in xrange(5):
        u = np.random.rand(2,1)
        norm_init = np.linalg.norm(gradient(A,u,b))
        L_k = [0 for i in xrange(20)]

        
        for k in xrange(20):
            grad = gradient(A, u, b)
            norm = np.linalg.norm(grad, 2)
            L_k[k] = norm / norm_init
            
            
            if (L_k[k] < 1e-2):
                break
            
            ro = norm**2/(grad.T * A * grad)
            u = u -  grad * ro
            
        
        plt.plot(L[: k + 1], L_k[: k + 1], 's', linestyle = '-', color = 'r');
  
    #plt.show()
    plt.savefig('lambda = ' + str(lambd) + '.png') 
            
def question_I_2_4(N):
    
    L = [i for i in xrange(N)]
    (x, y) = np.random.rand(2)
    L_k = [0 for i in range(N)]
    for i in xrange(N):
        ro = 20.0
        grad = gradient_Ros(x,y)
        p = 0

        while(Ros(x - ro * grad[0], y - ro * grad[1]) > Ros(x,y) and (p < 20)):
            ro = ro / 2.0
            p += 1
        
        x = x - ro * grad[0]
        y = y - ro * grad[1]
        
        L_k[i] = Ros(x, y)   
    print(x,y)   
    plt.plot(L[0:N:10], L_k[0:N:10], 's', linestyle = '-', color = 'r');
    
    
    
    