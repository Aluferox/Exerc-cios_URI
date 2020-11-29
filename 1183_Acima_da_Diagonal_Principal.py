# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
O = input()
soma = 0
cont_media = 0

for i in range(12):
    for j in range(12):
        N = float(input())
        if j > i:
            soma += N
            cont_media += 1

if(O.upper() == 'S'):
    print("{:.1f}".format(soma))
elif(O.upper() == 'M'):
    media = soma / cont_media
    print("{:.1f}".format(media))