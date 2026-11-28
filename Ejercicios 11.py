import math

numero = int(input("Introduce un número: "))

if numero < 2:
    es_primo = False
else:
    es_primo = True
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")