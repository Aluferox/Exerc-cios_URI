# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
while True:
    n, m = input().split(' ')
    n = int(n)
    m = int(m)

    if (n+m) == 0:
        break

    matriz = [input() for i in range(n)]

    a, b = input().split(' ')
    a= int(a)
    b= int(b)

    aux = [i for i in matriz for j in range((a - (n-n)) // n)]

    for j in aux:
        linha = ''
        for g in range(len(j)):
            linha += j[g] * ((b - (m-m)) // m)
        print(linha)
    print()




