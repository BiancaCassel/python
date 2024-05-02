import random

# Variáveis globais para armazenar a quantidade de itens
itens_comuns = 0
itens_raros = 0
itens_lendarios = 0

def abrir_caixa():
    global itens_comuns, itens_raros, itens_lendarios

    # Simulando a abertura da caixa com as probabilidades dadas
    sorteio = random.randint(1, 100)
    if sorteio <= 80:
        print("Você coletou 1 item comum!")
        itens_comuns += 1
    elif sorteio <= 99:
        print("Você coletou 1 item raro!")
        itens_raros += 1
    else:
        print("Você coletou 1 item lendário!")
        itens_lendarios += 1

def consultar_itens():
    global itens_comuns, itens_raros, itens_lendarios
    print("Itens comuns:", itens_comuns)
    print("Itens raros:", itens_raros)
    print("Itens lendários:", itens_lendarios)

def menu():
    print("1 – Abrir uma caixa")
    print("2 – Consultar itens")
    print("0 - Sair")

def main():
    while True:
        menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 0:
            print("Saindo...")
            break
        elif opcao == 1:
            abrir_caixa()
        elif opcao == 2:
            consultar_itens()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
