# Lendo a cotação do dólar para real
cotacao_dolar = int(input("Digite a cotação do dólar para real: "))


# Lendo a quantidade de dólares que o turista deseja comprar
quantidade_dolares = int(input("Digite a quantidade de dólares que deseja comprar: "))


# Calculando o valor total em reais que o turista precisará pagar
valor_total_reais = cotacao_dolar * quantidade_dolares


# Exibindo o valor total em reais
print("O valor total em reais que você precisará pagar é:", valor_total_reais)
