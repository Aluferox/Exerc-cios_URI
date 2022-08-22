# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
media = 0
cont_media = 0

while True:
     idade = float(input())
     if idade < 0:
         break

     if idade >= 0:
         media += idade
         cont_media += 1
print('{:.2f}'.format(media /cont_media))

