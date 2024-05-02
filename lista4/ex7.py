# Lista para armazenar os nomes informados pelo usuário
nomes = []

# Solicitando ao usuário que insira os cinco nomes
for i in range(5):
    nome = input("Digite o {} nome: ".format(i+1))
    nomes.append(nome)

# Encontrando o primeiro nome em ordem alfabética
primeiro_nome = min(nomes)

# Imprimindo o primeiro nome em ordem alfabética
print("O primeiro nome em ordem alfabética é:", primeiro_nome)
