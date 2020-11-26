# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
while True:
    num_seq = int(input())
    if num_seq == 0:
        break

    saida = ''
    for i in range(1,num_seq+1):
        saida += (str(i)+' ')
    print(saida.rstrip())

