#da la tablas de multiplicar del 1 al 5
numero = 1
while numero <= 5:
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    numero = numero + 1