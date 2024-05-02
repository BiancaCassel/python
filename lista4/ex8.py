def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

while True:
    # Solicitando ao usuário que insira um número
    numero = int(input("Entre com um número: "))
    
    # Calculando o fatorial do número fornecido
    resultado = calcular_fatorial(numero)
    
    # Imprimindo o resultado
    print(f"O fatorial de {numero} é {resultado}")
    
    # Perguntando ao usuário se deseja calcular outro número
    continuar = input("Calcular outro número (s/n)? ").strip().lower()
    
    # Se o usuário não deseja continuar, sair do loop
    if continuar != 's':
        break
