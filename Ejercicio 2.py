import random

numero = random.randint(1, 100)
intentos = 0

while intentos < 10:
    n = int(input("Número: "))
    intentos = intentos + 1
    if n == numero:
        print("Acertaste en", intentos, "intentos")
        break
    if numero > n:
        print("El número es mayor")
    else:
        print("El número es menor")
    print("Te quedan", 10 - intentos, "intentos")

if n != numero:
    print("Perdiste. El número era", numero)