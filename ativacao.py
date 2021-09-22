import numpy as np
# transfer function
# determinar a saida de uma camada

# PROBLEMAS LINEARMENTE SEPARAVEIS (N USA EM DEEP LEARNING)
def stepFunction(soma):
  if(soma >= 1):
    return 1
  else:
    return 0 

teste = stepFunction(30)

print (teste)

# --------------------------------------------
# PROBLEMAS DE CLASSIFICACAO BINARIA (0 E 1)
def sigmoidFunction(soma):
  return 1 / (1 + np.exp(-soma))

teste = sigmoidFunction(0.38)

print(teste)

# --------------------------------------------
# CLASSIFICACAO ENTRE -1 E 1
def hiperbolicTangent(soma):
  return (np.exp(soma) - np.exp(-soma)) /(np.exp(soma) + np.exp(-soma))

teste = hiperbolicTangent(-0.358)

print (teste)

# --------------------------------------------
# REDES NEURAIS CONVOLUCIONAIS 
def relu(soma):
  if (soma >= 0):
    return soma
  else:
    return 0

teste = relu(0.358)

print (teste)

# --------------------------------------------
# NAO FAZ NADA (USADA EM PROBLEMAS DE REGRESSAO)
def linear(soma):
  return soma

teste = linear(-0.5)

print (teste)
# --------------------------------------------
# CLASSIFICAO QUANDO SE TEM MAIS DE DUAS CLASSES
def softmax(x):
  ex = np.exp(x)
  return ex / ex.sum()

valores = [5, 2, 1.3]

print (softmax(valores))