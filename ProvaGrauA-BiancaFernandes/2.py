def divisivelPorN(numero, divisor):

    if divisor == 0:
        print("Não é possível efetuar divisão por zero.")

        return False
    
    elif numero % divisor == 0:
        return True
    else:
        return False


numero = 10
divisor = 5
print(divisivelPorN(numero, divisor)) 
