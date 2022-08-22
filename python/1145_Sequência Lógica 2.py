# -*- coding: utf-8 -*-
'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
x, y = input().split(' ')

x = int(x)
y = int(y)

cont = 0
aux = ''
for i in range(1,y+1):
    if cont==x:
       print(aux.rstrip())
       aux = ''
       cont = 0
    aux += str(i)+' '
    cont += 1
print(aux.rstrip())