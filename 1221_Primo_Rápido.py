# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from math import sqrt
casos = int(input())
aux = 0
for i in range(casos):
     num = int(input())
     if num == 2:
         print('Prime')
         continue
     for j in range(2, num + 1):
         if num % j == 0:
             print('Not Prime')
             break
         if (j > sqrt(num)):
                 print('Prime')
                 aux = 1
                 break