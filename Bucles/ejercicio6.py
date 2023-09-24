n = int(input("Introduce la altura del triangulo (Un numero entero positivo): "))

for i in range(n):
    for j in range (i+1):
        print("*", end="")
    print("")