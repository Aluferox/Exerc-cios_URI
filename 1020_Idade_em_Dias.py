dias = int(input())
anos = int(dias / 365)
meses = int((dias%365) / 30)
dias = (dias%365)%30

print('{0} ano(s)\n{1} mes(es)\n{2} dia(s)'.format(anos, meses, dias) )