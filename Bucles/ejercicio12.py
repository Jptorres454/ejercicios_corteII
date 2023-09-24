frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")
contador = 0

for i in frase:
    if i == letra:
        contador += 1
print(f"La letra {letra} aparece {contador} veces en la frase {frase}")