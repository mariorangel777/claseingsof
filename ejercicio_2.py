# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:56:31 2018

@author: beto_
"""

#devolver la lista que sus numeros sumados es más grande de una lista de listas

liston=[[1,2,3],[4,5,6],[10,11,12],[7,8,9],[52,-50]]



def sumi(listin):
    i=0
    sumin=0
    for each in listin:
        sumin+=listin[i]
        i+=1
    return sumin

def masgran(listin):
    i=0
    temp=0
    mayor=0
    lista=[]
    for each in listin:
        temp=sumi(listin[i])
        if temp > mayor:
            mayor= temp
            lista=listin[i]
        i+=1    
    return lista

listosa=[1,2,3,4]
print(masgran(liston))


















