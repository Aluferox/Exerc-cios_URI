# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
tentativas = int(input())
for j in range(tentativas):
    aux = list(input())
    aux4 =''
    for i in aux:
        if not i.isdigit() and i.isalpha():
            aux3 = ord(i)
            aux4 += chr(int(aux3)+3)

        else:
            aux4 += str(i)

    aux5 = aux4[::-1]
    aux6 = (len(aux5) // 2)
    aux7 = aux5[aux6:]
    aux_t = aux5[:aux6]
    aux8 = list(aux7)
    aux9 = []
    aux10 = ''
    cont = 0
    for i in aux8:
        aux9.append(int(ord(i)-1))
        aux10 += chr(aux9[cont])
        cont += 1
    print(aux_t + aux10)
