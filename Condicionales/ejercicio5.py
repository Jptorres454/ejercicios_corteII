nombre = input("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))
ingresos = float(input("Cual es tu ingreso semanal: "))

if edad >= 16 and ingresos >= 1000:
    print(f"Tienes que tributar {nombre}")
elif edad <= 16 or ingresos <= 1000:
    print(f"No tienes que cotizar {nombre}")