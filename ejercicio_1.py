# -*- coding: utf-8 -*-
"""
Created on Wed May 16 19:32:48 2018

@author: beto_
"""

def invertir (cadena):
    cadena=cadena.lower()
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        if cadena[indice] == "," or cadena[indice]==" ":
            indice = indice + (-1)
            cont -= 1                 
        else:
            invertida += cadena[indice]
            indice = indice + (-1)
            cont -= 1
    return invertida

def sincomas(cadena):
    cadena=cadena.lower()
    ninvertida = ""
    #cont = len(cadena)
    indice = 0
    for each in cadena:
        if cadena[indice] == "," or cadena[indice]==" ":
            indice+=1
            
        else:
            ninvertida += cadena[indice]
            indice +=1
           
    return ninvertida


def palindromo (cadena):
    palabra_invertida = invertir (cadena)
    cadena= sincomas(cadena)
    indice = 0
    cont = 0
    for i in range (len(cadena)):
        if palabra_invertida[indice] == cadena[indice]:
            indice += 1
            cont += 1
        else:
            return "No es palindromo"
            break

        if cont == len(cadena): #Si el contador = a la cantidad de letras de la cadena
            return "Es palindromo" 
        

cadenon="AnitA lAvA La Tina"
cadenosin="YO doNo Rosas, ORO nO doY"
print(palindromo(cadenosin))





