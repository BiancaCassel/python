# Função para calcular a média considerando o sistema de notas da Unisinos
def calcular_media(a, b, c):
    # Verificando se a nota A ou B deve ser substituída
    if c > a:
        a = c
    elif c > (2 * b):
        b = c / 2
    
    # Calculando a média
    media = (a + 2 * b) / 3
    
    # Verificando se o aluno está aprovado
    if media >= 7:
        return "APROVADO"
    else:
        return "REPROVADO"

# Variável para armazenar a soma das médias dos alunos
soma_medias = 0

# Lendo o número de alunos da Unisinos
num_alunos = int(input("Digite o número de alunos: "))

# Iterando sobre cada aluno
for aluno in range(1, num_alunos + 1):
    print(f"Aluno {aluno}:")
    
    # Lendo as notas do aluno
    nota_a = float(input("Digite a nota do grau A: "))
    nota_b = float(input("Digite a nota do grau B: "))
    nota_c = float(input("Digite a nota do grau C: "))
    
    # Calculando a média e verificando se o aluno está aprovado
    resultado = calcular_media(nota_a, nota_b, nota_c)
    
    # Imprimindo o resultado
    print("Resultado:", resultado)
    
    # Adicionando a média do aluno à soma das médias
    soma_medias += (nota_a + 2 * nota_b) / 3

# Calculando a média geral dos alunos
media_geral = soma_medias / num_alunos

# Imprimindo a média geral
print("Média geral dos alunos:", media_geral)
