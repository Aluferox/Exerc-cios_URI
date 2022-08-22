# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
numero = int(input())
for count in range(6):
  if numero % 2 == 0:
    numero += 1
    print (numero)
  else :
    numero += 2
    print (numero)