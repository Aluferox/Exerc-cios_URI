# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
while True:
    quantidadeAlunos = int(input())

    if quantidadeAlunos == 0:
        break
    listaAlunos = input().split()
    primeiroAluno = int(input())

    while True:
        alunos = int(listaAlunos[primeiroAluno-1])

        if alunos == primeiroAluno:
            print(listaAlunos[primeiroAluno-1])
            break
        else:
            primeiroAluno  = alunos