# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:09:46 2018

@author: beto_
"""



main_dir="C:\\Users\\beto_\\OneDrive\\Mineria de datos\\examen"
archivo="\\paises.txt"
listaf=[]
lista1=[]
with open(main_dir+archivo, 'r', encoding='utf-8') as content_file:
    lista1=content_file.readlines()

for each in lista1:
    listaf.append(each.split())
#print(listaf)




def encontrar(cadena):
    i=0
    j=0
    for each in listaf:
        for each in listaf[i]:
            if cadena == each:
                return listaf[i][0]
            else:
                j+=1
        i+=1
    return "No lo sé bro, busca en google"


#print(encontrar("Guanajuato"))
print(encontrar("Huanaxhuato"))

#lista de listas
#el 0 siempre será el pais
#si cadena = paises[i][j]
#return piases[i][0]
#else return "No lo sé bro, espero haberte ayudado"
#
#
#
#
#
#
#
#



