inferior = int(input("Límite inferior: "))
superior = int(input("Límite superior: "))

while inferior > superior:
    print("El límite inferior no puede ser mayor que el superior.")
    inferior = int(input("Límite inferior: "))
    superior = int(input("Límite superior: "))

suma = 0
fuera = 0
igual_limite = False

numero = int(input("Número (0 para terminar): "))

while numero != 0:
    if inferior < numero < superior:
        suma += numero
    elif numero < inferior or numero > superior:
        fuera += 1
    else:
        igual_limite = True
    numero = int(input("Número (0 para terminar): "))

print("Suma de los números dentro del intervalo:", suma)
print("Números fuera del intervalo:", fuera)
if igual_limite:
    print("Se ha introducido algún número igual a un límite.")
else:
    print("No se ha introducido ningún número igual a los límites.")