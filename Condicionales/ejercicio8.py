bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6

puntos = float(input("Introduce tu puntuación: "))

if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos == meritorio:
    nivel = "Meritorio"
else:
    nivel = ""

if nivel == " ":
    print("Esta puntuación no es valida")
else:
    print("T nivel de rendimiento es %s" %nivel)
    print(f"Te corresponde cobrar: {(puntos * bonificacion)}")
