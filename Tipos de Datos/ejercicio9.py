cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))

cantidad_invertida = (cantidad * (interes / 100 + 1)) ** años

print(f"Capital final: {cantidad_invertida}")