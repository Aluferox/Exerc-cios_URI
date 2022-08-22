"""
Você terá como uma entrada várias linhas, cada uma com uma string. O valor de cada caracter é computado como segue:
Valor = (Posição no alfabeto) + (Elemento de entrada) + (Posição do elemento)
Todas posições são baseadas em zero. 'A' tem posição 0 no alfabeto, 'B' tem posição 1 no alfabeto, ... O cálculo de hash retornado
é a soma de todos os caracteres da entrada. Por exemplo, se a entrada for:
CBA
DDD
então cada caractere deverá ser computado como segue:

2 = 2 + 0 + 0 : 'C' no elemento 0 posição 0
2 = 1 + 0 + 1 : 'B' no elemento 0 posição 1
2 = 0 + 0 + 2 : 'A' no elemento 0 posição 2
4 = 3 + 1 + 0 : 'D' no elemento 1 posição 0
5 = 3 + 1 + 1 : 'D' no elemento 1 posição 1
6 = 3 + 1 + 2 : 'D' no elemento 1 posição 2

O cálculo final de hash será 2+2+2+4+5+6 = 21.
"""

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
casos_de_teste = int(input())

def arrayHash(hash, elemEntrada):
    valorHash = 0
    for index, value in enumerate (hash):
        valorHash += alfabeto.index(value)+ elemEntrada+ index
    return valorHash


for teste in range(casos_de_teste):
    quantHash = int(input())
    valorHashFinal = 0
    for linhas in range(quantHash):
        valorHashFinal += arrayHash(input(), linhas)
    print(valorHashFinal)