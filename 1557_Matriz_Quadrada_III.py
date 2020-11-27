# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
import math
while True:
     matriz = []
     ordem = int(input(''))
     if(ordem == 0):
         break
     else:
         for i in range(ordem):
             linha = []
             for j in range(ordem):
                linha.append(pow(2,i + j))
             matriz.append(linha)
         len_matriz = len(str(matriz[i][i]))
     for linha in matriz:
         for a in range(ordem):
             if a < ordem - 1:
                 print('{:{}}'.format(linha[a], len_matriz), end=' ')
             else:
                 print('{:{}}'.format(linha[a], len_matriz))
     print()