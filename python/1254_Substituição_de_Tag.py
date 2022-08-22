import  re
while True:
    try:
        a = input().lower()
        d = input()
        g = input()
        b = g.count('>')
        c = g.count('<')
        f = ''
        h = ''
        string_junta = ''
        lista_trocar = []
        tesoura_lista = []
        if '<' in g:
            for verificacao in g:
                if verificacao == '<' or verificacao == '>':
                    h += verificacao
            if '<' in g or '>' in g:
                if '<<' not in h:
                    if '>>' not in h:
                        if (b+c) % 2 == 0:
                            for tag in g:
                                if '<' in tag:
                                    f += ',' + tag
                                elif '>' not in tag:
                                    f += tag
                                else:
                                    f += tag + ','
                    tesoura_lista = f.split(',')
                    tesoura_lista = [i for i in tesoura_lista if i]
                    montagem =''
                    for h in tesoura_lista:
                        if '<' in h:
                            q = re.compile(a, re.IGNORECASE)
                            montagem += q.sub(d, h)
                        else:
                            montagem += h
                    print(montagem)
        else:
            print(g)
    except EOFError:
        break
