#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:01:53 2024

@author: gary-montes
"""
def operaciones (a):
    # tablas de multiplicar
    
    b=None
    for i in range(1,10):
        b=a*i
        print(f'{a} x {i}= {b}')
    
    print('Fin de la tabla de multiplicar')

print(__name__)

if __name__=='__main__':

    c=int(input('Ingrese la tabla de multiplicar: '))    
    operaciones(c)
    operaciones(10)
    

        


