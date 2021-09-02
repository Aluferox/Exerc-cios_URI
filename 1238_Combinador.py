def tamanhos_iguais(palavraUm, palavraDois):
    cadeiaResultante = ''
    for indice in range(len(palavraUm)):
        cadeiaResultante += palavraUm[indice] + palavraDois[indice]
    return cadeiaResultante

def tamanhos_diferentes(palavraUm, palavraDois):
    cadeiaResultante = ''

    if len(palavraUm) > len(palavraDois):
        tamanhoPalavraDois = len(palavraDois)
        for index in range(len(palavraDois)):
            cadeiaResultante += palavraUm[index] + palavraDois[index]
        cadeiaResultante += palavraUm[tamanhoPalavraDois:]
    else:
        tamanhoPalavraUm = len(palavraUm)
        for index in range(len(palavraUm)):
            cadeiaResultante += palavraUm[index] + palavraDois[index]
        cadeiaResultante += palavraDois[tamanhoPalavraUm:]
    return cadeiaResultante

casosDeTeste = int(input())
for quantidade in range(casosDeTeste):

    cadeiaDeCaracteres = input()
    palavra_um, palavra_dois = cadeiaDeCaracteres.split(' ')

    if len(palavra_um) == len(palavra_dois):
        print(tamanhos_iguais(palavra_um, palavra_dois))
    else:
        print(tamanhos_diferentes(palavra_um, palavra_dois))





