# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
vetor_fibo = [0,1]
vetor_chamadas = [1,1]
atual = 1
anterior = 0
for i in range(39):
    atual = atual + anterior
    anterior = atual -anterior
    vetor_fibo.append(atual)
atual = 1
anterior = 1
for i in range(39):
     novo = atual + anterior + 1
     vetor_chamadas.append(novo)
     anterior = atual
     atual = novo

caso_testes = int(input())
for i in range(caso_testes):
    num = int(input())
    print('fib({}) ='.format(num),'{}'.format(vetor_chamadas[num]-1),'calls = {}'.format(vetor_fibo[num]))