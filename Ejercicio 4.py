
ncantidad = int(input("Indique la cantidad de números que introducirá: "))

# Inicializamos los contadores a 0
positivo = 0
negativo = 0
igual = 0

while ncantidad > 0:
    # Pedimos un número al usuario
    n = int(input("Introduce un número: "))

    # Comprobamos si el número es negativo
    if n < 0:
        negativo = negativo + 1

    # Comprobamos si el número es positivo
    elif n > 0:
        positivo = positivo + 1

    # Si no es positivo ni negativo, es igual a 0
    else:
        igual = igual + 1

    # Restamos uno para indicar que queda un número menos
    ncantidad = ncantidad - 1

# Mostramos los resultados al terminar el bucle
print("Los números positivos son: ", positivo)
print("Los números negativos son: ", negativo)
print("Los números 0 son: ", igual)

