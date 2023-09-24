usuario = input("Cual es tu nombre: ")
altura = float(input("Cuanto mides: "))
kg = float(input("Cuanto pesas: "))

imc = kg/altura**2

print(f"Este es tu indice de masa corporal {usuario}: {imc}")