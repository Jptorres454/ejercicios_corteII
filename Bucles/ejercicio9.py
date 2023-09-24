contraseña_correcta = "contraseña"

for intento in range (3):
    contraseña = input("Introduce tu contraseña: ")

    if contraseña == contraseña_correcta:
        print("¡CONTRASEÑA CORRECTA!")
        break
    else:
        print("¡CONTRASEÑA INCORRECTA! D:")

if contraseña != contraseña_correcta:
    print("Has agotado tus intentos.")