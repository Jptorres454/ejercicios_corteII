nombre = input("Por favor, ingresa tu nombre: ")
sexo = input("Ingresa tu sexo (M para mujer, H para hombre): ")

nombre = nombre.upper()

if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre >= "N"):
    grupo = "A"
else:
    grupo = "B"

print(f"Tu nombre es {nombre} y perteneces al grupo {grupo}")