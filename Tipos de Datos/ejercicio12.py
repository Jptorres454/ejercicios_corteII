barra_de_pan = 3.49
descuento = 0.6

barras_compradas = int(input("¿Cuantas barras de pan va a comprar?"))
resultado = barras_compradas * barra_de_pan
resultado_descuento = resultado * descuento

print(f"""Bienvenido:
\n * El numero de panes a comprar: {barras_compradas}
\n * El precio a pagar sin el resultado: {resultado}
\n * El precio con el 60% de descuento: {resultado_descuento}""")