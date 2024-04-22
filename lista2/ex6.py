
def calcular_arrecadacao():
    smartphones_vendidos = int(input("Digite o número de smartphones vendidos: "))
    tablets_vendidos = int(input("Digite o número de tablets vendidos: "))
    preco_smartphone = 1000.00
    preco_tablet = 1500.00
    total_arrecadado = (smartphones_vendidos * preco_smartphone) + (tablets_vendidos * preco_tablet)
    print("Total arrecadado: R$ {:.2f}".format(total_arrecadado))

# Chamar a função para testar
calcular_arrecadacao()

