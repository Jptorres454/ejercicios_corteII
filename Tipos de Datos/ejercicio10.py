payasos = int(input("Introduce el número de payasos a enviar: "))
muñecas = int(input("Introduce el número de muñecas a enviar: "))

peso_payasos = 112
peso_muñecas = 75

peso_total = peso_payasos * payasos + muñecas * peso_muñecas

print(f"El peso total del paquete es: {peso_total}")