import random

def sorteio(inicio, fim):
    numero_sorteado = random.randint(inicio, fim)
    return numero_sorteado

# Exemplo de uso da função
inicio_intervalo = 10
fim_intervalo = 20
numero_sorteado = sorteio(inicio_intervalo, fim_intervalo)
print("Número sorteado:", numero_sorteado)
