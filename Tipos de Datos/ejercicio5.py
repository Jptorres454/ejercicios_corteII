usuario = input("Nombre del usuario: ")
print(f"Hola {usuario}, la hora se paga por 60 dolares.")
horas_trabajadas = float(input("Escribe el numero de horas trabajadas en esta semana: "))

paga = horas_trabajadas*60

print(f"""Este es tu paga por el numero de horas trabajadas: 
      \n * Trabajador: {usuario}
      \n * Horas trabajadas: {horas_trabajadas}
      \n * Paga por la semana: {paga}""")