n = int(input("Escribe un numero entero: "))
m = int(input("Escribe otro numero entero: "))

division = n / m 
cociente = n // m 
resto = n % m

print(f"""Se genero una division:
\n * El resultado de la division es:  {division}
\n * El cociente de la division es: {cociente}
\n * El resto de la division es: {resto}""")