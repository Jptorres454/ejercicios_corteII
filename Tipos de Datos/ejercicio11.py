cuenta = float(input("Escribe cuanto vas a ingresar a tu cuenta: "))
interes = 0.04

interes_año1 = cuenta * (1 + interes)
interes_año2= interes_año1 * (1 + interes)
interes_año3 = interes_año2 * (1 + interes)

print(f"""Este es el interes que genera alrededor de los años:
\n * Interes en el primer año: {interes_año1}
\n * Interes en el segundo año: {interes_año2}
\n * Interes en el tercer año: {interes_año3}""")