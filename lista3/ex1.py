def realizar_divisao(dividendo, divisor):
    if divisor != 0:
        resultado = dividendo / divisor
        print("O resultado da divisão é:", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")

def main():
    try:
        dividendo = float(input("Digite o dividendo: "))
        divisor = float(input("Digite o divisor: "))
        realizar_divisao(dividendo, divisor)
    except ValueError:
        print("Erro: Certifique-se de inserir números válidos.")

if __name__ == "__main__":
    main()
