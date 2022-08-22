"""

Júlio César usava um sistema de criptografia, agora conhecido como Cifra de César, que trocava cada letra pelo
equivalente em duas posições adiante no alfabeto (por exemplo, 'A' vira 'C', 'R' vira 'T', etc.). Ao final do
alfabeto nós voltamos para o começo, isto é 'Y' vira 'A'. Nós podemos, é claro, tentar trocar as letras com
quaisquer número de posições.

"""
pos_Ascii = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

palavra = ''

def cifra_cesar(sentencaCodificada, deslocamento):
  palavra = ''
  for char in sentencaCodificada:
      index = pos_Ascii.index(char)
      index -= deslocamento
      palavra += pos_Ascii[index]
  print(palavra)

casosDeTeste = int(input())
for testes in range(casosDeTeste):
    sentencaCodificada = input()
    deslocamento = int(input())

    for char in sentencaCodificada:
        if deslocamento == 0:
            print(sentencaCodificada)
            break
        if deslocamento == 25:
            aux = pos_Ascii.index(char)+1
            if aux >= len(pos_Ascii):
                palavra += pos_Ascii[0]
            elif aux == 0:
                palavra += pos_Ascii[25]
            else:
                palavra += pos_Ascii[aux]
        else:
            cifra_cesar(sentencaCodificada, deslocamento)
            break
    if len(palavra) > 1:
        print(palavra)
    palavra = ''



