import random

# Inicializando contadores
positivos = 0
negativos = 0

# Sorteando e imprimindo os números inteiros
for _ in range(20):
    numero = random.randint(-10, 10)
    if numero > 0:
        print(numero, "POSITIVO")
        positivos += 1
    elif numero < 0:
        print(numero, "NEGATIVO")
        negativos += 1
    else:
        print(numero, "NULO")

# Imprimindo a quantidade de números positivos e negativos
print("Quantidade de números positivos:", positivos)
print("Quantidade de números negativos:", negativos)
