while True:
    # Solicitando ao usuário para inserir um número de 1 a 9
    numero = int(input("Entre com um número de 1 a 9: "))
    
    # Verificando se o número está dentro do intervalo válido
    if 1 <= numero <= 9:
        # Mostrando a tabuada de multiplicação do número
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
        
        # Perguntando ao usuário se deseja calcular outro número
        continuar = input("Calcular outro número (s/n)? ").strip().lower()
        
        # Se o usuário não deseja continuar, sair do loop
        if continuar != 's':
            break
    else:
        print("Número inválido. Por favor, insira um número de 1 a 9.")
