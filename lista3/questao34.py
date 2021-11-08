def calculate_power(base, exp):
    if(exp == 1):
        return base
    if(exp % 2 == 0):
        number = calculate_power(base, exp / 2)
        return number * number
    else:
        number = calculate_power(base, (exp - 1) / 2) 
        return base * number * number

result = calculate_power(2, 6)
print(result)
# o algoritmo imprime 64
