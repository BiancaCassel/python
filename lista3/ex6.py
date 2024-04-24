import random

def verificar_resultado(escolha_usuario, numero_usuario, numero_sorteado):
    soma = numero_usuario + numero_sorteado
    resultado = soma % 2 == 0 if escolha_usuario == "PAR" else soma % 2 != 0
    return resultado

def jogo_par_impar():
    escolha_usuario = input("Você escolhe PAR ou ÍMPAR? ").upper()
    if escolha_usuario not in ["PAR", "ÍMPAR"]:
        print("Escolha inválida. Por favor, escolha entre PAR ou ÍMPAR.")
        return

    numero_usuario = int(input("Digite um número de 0 a 5: "))
    if numero_usuario < 0 or numero_usuario > 5:
        print("Número inválido. Por favor, digite um número entre 0 e 5.")
        return

    numero_sorteado = random.randint(0, 5)
    print(f"O número sorteado foi: {numero_sorteado}")

    if verificar_resultado(escolha_usuario, numero_usuario, numero_sorteado):
        print("Você venceu!")
    else:
        print("O programa venceu!")

# Executar o jogo
jogo_par_impar()
