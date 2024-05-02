# Pedindo ao usuário para inserir a quantidade de números a serem lidos
n = int(input("Digite a quantidade de números a serem lidos: "))

# Inicializando a variável para armazenar a soma
soma = 0

# Lendo os números e calculando a soma
for i in range(n):
    numero = float(input("Digite o {} número: ".format(i+1)))
    soma += numero

# Imprimindo a soma dos números lidos
print("A soma dos números lidos é:", soma)
