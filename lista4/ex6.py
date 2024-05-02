import random

# Sorteando 5 valores entre 0 e 100
valores = [random.randint(0, 100) for _ in range(5)]

# Encontrando o menor e o maior valor
menor = min(valores)
maior = max(valores)

# Calculando a média
media = sum(valores) / len(valores)

# Imprimindo os resultados
print("Valores sorteados:", valores)
print("Menor valor:", menor)
print("Maior valor:", maior)
print("Média dos valores:", media)
