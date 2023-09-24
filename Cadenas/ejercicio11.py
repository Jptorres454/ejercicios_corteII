producto = input("Introduce el nombre del producto marca ACME: ")
precio = float(input("Introduce el precio: "))
unidades = int(input("Introduce el numero de unidades: "))

total = precio * unidades

cadena = f"{producto}: {unidades:5d} unidades x {precio:6.2f}€ = {total:8.2f}€"

print(cadena)