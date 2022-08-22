import math

delta = None
X_duas_Linhas = None
A = None
B = None
X_uma_Linha = None
C = None
lista_bhaskara = None

def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()


lista_bhaskara = read_line().split(" ")
A = float((lista_bhaskara[0]))
B = float((lista_bhaskara[1]))
C = float((lista_bhaskara[2]))
if A != 0:
  delta = (math.pow(B, 2)) - 4 * (A * C)
  if delta > 0:
    X_uma_Linha = "{:0.5f}".format(((B * -1 + (math.sqrt(delta))) / (2 * A)))
    print(str("R1 = ") + str(X_uma_Linha))
    X_duas_Linhas = "{:0.5f}".format(((B * -1 - (math.sqrt(delta))) / (2 * A)))
    print(str("R2 = ") + str(X_duas_Linhas))
  elif delta < 0:
    print(str("Impossivel calcular") + str(''))
else:
  print(str("Impossivel calcular") + str(''))
