# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
N = int(input())
total = 0
R = 0
C = 0
S = 0
for i in range(N):
	Q = input().split(" ")
	tipo = Q[1]
	N = int(Q[0])
	total += N
	if(tipo.upper() == 'R'):
		R += N
	elif(tipo.upper() == 'C'):
		C += N
	elif(tipo.upper() == 'S'):
		S += N
print("Total: " + str(total) + " cobaias" )
print("Total de coelhos: "+ str(C))
print("Total de ratos: " + str(R))
print("Total de sapos: " + str(S))

print("Percentual de coelhos: {:.2f}".format((C / total) * 100),"%")
print("Percentual de ratos: {:.2f}".format((R / total) * 100),"%")
print("Percentual de sapos: {:.2f}".format((S / total) * 100),"%")