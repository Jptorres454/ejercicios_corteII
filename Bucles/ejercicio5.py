invertir = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años? "))

for i in range(años):
    invertir *= 1 + interes / 100
    i += 1
    print("capital tras", i, "años: ", round(invertir, 2))