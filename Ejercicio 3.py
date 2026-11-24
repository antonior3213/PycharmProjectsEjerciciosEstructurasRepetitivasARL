n = int(input("Ingrese un numero: "))
suma = 0
cantidad = 0
while n != 0:
    suma = suma + n
    cantidad = cantidad + 1
    n = int(input("Ingrese un numero: "))
if cantidad != 0:
    division = suma / cantidad
    print("La suma es ", suma)
    print("La cantidad es ", cantidad)
    print("La media es ", division)
else:
    print("No se introdujo ningún número")