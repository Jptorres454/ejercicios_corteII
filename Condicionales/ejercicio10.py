print("""BIENVENIDO A LA PIZZERIA J DE LA TORRE.
>>>TIPOS DE PIZZA
      1. Vegetariana
      2. No vegetariana
""")

tipo = int(input("Ingrese el numero correspondiente al tipo de pizza que quieres:"))

if tipo == 1:
    print("""INGREDIENTES DE PIZZA VEGETARIANA.
          1. Pimiento
          2. Tofú""")
    ingrediente = int(input("Introduce el ingrediente que deseas: "))
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == 1:
        print("Pimiento")
    else:
        print("Tofú")

else:
    print("""INGREDIENTES DE PIZZA NO VEGETARIANA.
          1. Jamon
          2. Salmón""")
    ingrediente = int(input("Introduce el ingrediente que deseas: "))
    print("Pizza no vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == 1:
        print("Jamón")
    else:
        print("Salmón")