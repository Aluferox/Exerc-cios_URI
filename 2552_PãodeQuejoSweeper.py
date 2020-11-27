# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
while True:
    try:
        linhas,colunas = map(int,input().split())
        matriz = []
        for L in range(linhas):
           linha = list(map(int,input().split()))
           matriz.append(linha)


        for i in range(len(matriz)):
            for j in range(colunas):
                val = 0
                if(i - 1 >= 0):
                     val += matriz[i - 1][j]
                if(i + 1 < linhas):
                     val += matriz[i + 1][j]
                if(j - 1 >= 0):
                     val += matriz[i][j - 1]
                if(j + 1 < colunas):
                     val += matriz[i][j + 1]
                if(matriz[i][j] == 1):
                     val = 9
                print(val,end='')
            print('')
    except EOFError:
        break