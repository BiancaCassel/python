# Solicitando ao usuário que insira o valor do divisor
divisor = int(input("Entre com o valor do divisor: "))

# Solicitando ao usuário que insira os limites do intervalo
inicio_intervalo = int(input("Início do intervalo: "))
final_intervalo = int(input("Final do intervalo: "))

# Inicializando uma lista para armazenar os números divisíveis
divisiveis = []

# Verificando os números divisíveis dentro do intervalo especificado
for numero in range(inicio_intervalo, final_intervalo + 1):
    if numero % divisor == 0:
        divisiveis.append(numero)

# Imprimindo os números divisíveis
print("Números divisíveis por", divisor, "no intervalo de", inicio_intervalo, "a", final_intervalo, ":")
print(*divisiveis)
