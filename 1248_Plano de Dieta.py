# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
casos_teste = int(input())
for i in range(casos_teste):
    dieta = list(input())
    cafe = input()
    almoco = list(input() + cafe)
    result = True
    for i in almoco:
        if i not in dieta:
            print('CHEATER')
            result = False
            break
        [dieta.pop(j) for j,f in enumerate(dieta) if i == f]
    if result:
        print(*sorted(dieta), sep='')