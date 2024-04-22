# Define os preços dos produtos
preco_camiseta = 25.00
preco_calca = 100.00
preco_cinto = 40.00

# Solicita ao usuário o número de camisetas, calças e cintos comprados
num_camisetas = int(input("Digite o número de camisetas compradas: "))
num_calcas = int(input("Digite o número de calças compradas: "))
num_cintos = int(input("Digite o número de cintos comprados: "))

# Calcula o valor total da compra
total_compra = (num_camisetas * preco_camiseta) + (num_calcas * preco_calca) + (num_cintos * preco_cinto)

# Calcula o desconto de 10% sobre o total
desconto = total_compra * 0.10

# Calcula o novo valor da compra com o desconto aplicado
valor_com_desconto = total_compra - desconto

# Exibe o valor do desconto e o valor final da compra
print("O valor do desconto é de R$", desconto)
print("O valor da compra com o desconto de 10% é de R$", valor_com_desconto)
