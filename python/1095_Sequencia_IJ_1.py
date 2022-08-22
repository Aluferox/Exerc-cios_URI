# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
vetor_i = []
vetor_j = []

for i in range(1,40,3):
   vetor_i.append(i)
for j in range(60,-5,-5):
       vetor_j.append(j)
for i in range(len(vetor_j)):
    print('I='+str(vetor_i[i])+' J='+str(vetor_j[i]))