# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

cont = 0
for i in range(1,10,2):
    for j in range(5,8,1)[::-1]:

        if(i == 1):
            print("I="+str(i),"J="+str(j))
        else:
            print("I="+str(i),"J="+str(j+cont))
    cont += 2