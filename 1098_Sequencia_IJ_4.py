# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
T = 0
for i in range(11):
    for j in range(1, 4):
        if (i == 0) or (i == 5) or (i == 10):
            print('I=%d J=%d' % (T , j + T))
        else:
            print('I={:.1f}'.format(T), 'J={:.1f}'.format(j + T))
    T += 0.2
    T = round(T,1)