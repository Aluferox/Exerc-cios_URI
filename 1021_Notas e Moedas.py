# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
total_notas = float(input())
for i in range(len(notas)):
    if  i == 0:
        print('NOTAS:')
    elif  i == 6:
        print('MOEDAS:')

    if i < 6:
        print('{total} nota(s) de R$ {:.2f}'.format(notas[i]   ,total= int(total_notas//notas[i])))
    elif i >= 6:
        print('{total} moeda(s) de R$ {:.2f}'.format(notas[i]   ,total= int(total_notas/notas[i])))
    total_notas = round(float(total_notas%notas[i]),2)
