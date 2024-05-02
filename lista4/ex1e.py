# Pedindo ao usuário para inserir 15 números
numeros = []
for i in range(15):
    numero = float(input("Digite o {} número: ".format(i+1)))
    numeros.append(numero)

# Calculando a soma dos números
soma = sum(numeros)

# Calculando a média dos números
media = soma / len(numeros)

# Escrevendo a soma e a média
print("A soma dos números é:", soma)
print("A média dos números é:", media)
