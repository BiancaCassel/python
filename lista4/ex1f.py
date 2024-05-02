# Pedindo ao usuário para inserir 10 números inteiros
numeros = []
for i in range(10):
    numero = int(input("Digite o {} número inteiro: ".format(i+1)))
    numeros.append(numero)

# Contando a quantidade de números pares e ímpares
pares = 0
impares = 0
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Escrevendo a quantidade de números pares e ímpares
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
