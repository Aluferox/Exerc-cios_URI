# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:
    try:
        total_palavras, num_max_linhas_por_pagina, num_max_caracteres_por_linha = (input().split())
        total_palavras = int(total_palavras)
        num_max_linhas_por_pagina = int(num_max_linhas_por_pagina)
        num_max_caracteres_por_linha = int(num_max_caracteres_por_linha)

        conto = (input())
        total_linhas = 0
        cont = num_max_caracteres_por_linha

        while cont < len(conto):
             while conto[cont] != ' ':
                cont -= 1
             if conto[cont] == ' ':
                cont += 1
                total_linhas += 1
             cont += num_max_caracteres_por_linha
        if (total_linhas+1) % num_max_linhas_por_pagina == 0:
            print(((total_linhas+1) // num_max_linhas_por_pagina))
        else:
            print(((total_linhas+1) // num_max_linhas_por_pagina) + 1)
    except EOFError:
        break


