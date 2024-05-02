# Solicitando ao usuário que insira o número de linhas e o caractere
n = int(input("Entre com um número: "))
caractere = input("Entre com um caractere: ")

# Loop para controlar o número de linhas
for i in range(1, n + 1):
    # Loop para imprimir os caracteres
    for j in range(i):
        print(caractere, end=" ")
    print()  # Mudando para a próxima linha após imprimir os caracteres
