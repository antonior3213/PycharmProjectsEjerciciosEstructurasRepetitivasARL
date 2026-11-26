base = float(input("Base: "))
exponente = int(input("Exponente (entero positivo): "))

while exponente <= 0:
    print("El exponente debe ser un entero positivo.")
    exponente = int(input("Exponente (entero positivo): "))

resultado = 1
for i in range(exponente):
    resultado *= base

print(f"{base} elevado a {exponente} = {resultado}")