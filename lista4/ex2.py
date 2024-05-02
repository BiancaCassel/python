import random

# Sorteando o número aleatório
numero_sorteado = random.randint(1, 10)

# Definindo o número máximo de tentativas
max_tentativas = 3

# Loop para as tentativas do usuário
for tentativa in range(1, max_tentativas + 1):
    # Solicitando a tentativa do usuário
    tentativa_usuario = int(input("Tentativa {}: Digite um número de 1 a 10: ".format(tentativa)))
    
    # Verificando se a tentativa está correta
    if tentativa_usuario == numero_sorteado:
        print("Parabéns! Você acertou o número.")
        break
    elif tentativa_usuario < numero_sorteado:
        print("O número a adivinhar está acima.")
    else:
        print("O número a adivinhar está abaixo.")

# Se o usuário não acertar após as 3 tentativas
else:
    print("Suas tentativas acabaram. O número a adivinhar era:", numero_sorteado)
