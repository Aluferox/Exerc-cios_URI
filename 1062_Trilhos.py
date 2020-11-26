# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
n = int(input())
vetor_saida = []
while n!=0:

    class pilha_class:
        def __init__(self):
            self.pilha = []
            self.estacaoo = []

        def estacao(self, elemento):
            self.pilha.append(elemento)

        def desempilha(self,e_igual):
            if self.pilha != [] and self.pilha[-1] == e_igual:
                return self.pilha.pop(-1)
            else:
                return False

    call_func = pilha_class()
    vagoes = list(map(int,input().split()))
    if vagoes == [0]:
        n = int(input())
        vetor_saida.append(0)
        continue

    alvo = len(vagoes)
    direcao_B = []
    for i in list(reversed(vagoes)):
        if i == alvo:
            direcao_B.append(i)
            alvo -= 1
        else:
            call_func.estacao(i)
        for j in range(alvo):
            if call_func.desempilha(alvo) == alvo:
                direcao_B.append(alvo)
                alvo -= 1
            else:
                break

    if alvo == 0:
         vetor_saida.append('Yes')
    else:
         vetor_saida.append('No')

for k in vetor_saida:
    if k == 0:
        print('')
    if k != 0:
        print(k)







