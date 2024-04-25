# Dicionário com os ingredientes e suas quantidades iniciais
ingredientes = {
    "Pó de Fênix": 100,
    "Essência Celestial": 50,
    "Raiz de Dragão": 45,
    "Orvalho Lunar": 30,
    "Flores secas": 200,
    "Elixir amargo": 20,
    "Lágrimas de unicórnio": 15
}

# Dicionário com as poções e seus ingredientes
pocoes = {
    1: {"nome": "Poção de Cura", "ingredientes": {"Pó de Fênix": 30, "Essência Celestial": 20, "Flores secas": 20, "Lágrimas de unicórnio": 10}},
    2: {"nome": "Poção Força da Floresta", "ingredientes": {"Orvalho Lunar": 20, "Raiz de Dragão": 30, "Flores secas": 30}},
    3: {"nome": "Poção Sabedoria da Riqueza", "ingredientes": {"Essência Celestial": 30, "Pó de Fênix": 50}},
    4: {"nome": "Poção Sorte no Amor", "ingredientes": {"Orvalho Lunar": 10, "Flores secas": 50, "Lágrimas de unicórnio": 5}},
    5: {"nome": "Poção Malvada", "ingredientes": {"Elixir amargo": 10, "Raiz de Dragão": 15}}
}

def consultar_ingredientes():
    print("Ingredientes disponíveis:")
    for ingrediente, quantidade in ingredientes.items():
        print(f"{ingrediente}: {quantidade} g/ml")

def preparar_pocao():
    int(input(" Escolha o número referente a poção que deseja preparar:\n 1-Poção de Cura.              Ingredientes:Pó de Fênix(30g),Essência Celestial(20 ml),Flores secas(20g),Lágrimas de unicórnio(10 ml)\n 2-Poção Força da Floresta.    Ingredientes: Orvalho Lunar (20 ml), Raiz de Dragão (30g), Flores secas (30g) \n 3-Poção Sabedoria da Riqueza. Ingredientes: Essência Celestial (30 ml), Pó de Fênix (50g)\n 4-Poção Sorte no Amor.        Ingredientes: Orvalho Lunar (10 ml), Flores secas (50g), Lágrimas deunicórnio (5 ml)\n 5-Poção Malvada.              Ingredientes: Elixir amargo (10 ml), Raiz de Dragão (15g) \n"))
    num_pocao = int(input("Digite o número da poção que deseja preparar: "))
    pocao = pocoes.get(num_pocao)
    if pocao:
        faltando_ingredientes = []
        for ingrediente, quantidade in pocao["ingredientes"].items():
            if ingredientes.get(ingrediente, 0) < quantidade:
                faltando_ingredientes.append(ingrediente)
        if faltando_ingredientes:
            print("Ingredientes insuficientes para preparar a poção. Faltando:")
            for ingrediente in faltando_ingredientes:
                print(ingrediente)
        else:
            for ingrediente, quantidade in pocao["ingredientes"].items():
                ingredientes[ingrediente] -= quantidade
            print("Poção criada com sucesso!")
    else:
        print("Número de poção inválido.")

# Função principal
def main():
    while True:
        print("\nMenu:")
        print("1. Preparar poção")
        print("2. Consultar ingredientes")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            preparar_pocao()
        elif opcao == "2":
            consultar_ingredientes()
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Executar o programa
if __name__ == "__main__":
    main()
