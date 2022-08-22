# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
while True:
    try:
        a = input()
        cont_tag_i = 0
        cont_tag_b = 0
        b = ''
        c = ''
        for i in range(len(a)):

            if a[i] == '_':
                if cont_tag_i % 2 == 0:
                    b += '<i>'
                    cont_tag_i += 1
                    continue

                else:
                    b += '</i>'
                    cont_tag_i += 1
                    continue
            elif a[i] == '*':
                if cont_tag_b % 2 == 0:
                    b += '<b>'
                    cont_tag_b += 1
                    continue
                else:
                    b += '</b>'
                    cont_tag_b += 1
                    continue

            b += a[i]
        print(b)
    except EOFError:
        break