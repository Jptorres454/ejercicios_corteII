print("\n BIENVENIDO A LA SALA DE JUEGOS ")
edad = int(input("Por favor ingresa tu edad: "))

if edad < 4:
    print("Puedes entrar gratis :D")
elif edad > 4 and edad <= 18:
    print("Debes pagar 5€")
elif edad > 18:
    print("Debes pagar 10€")