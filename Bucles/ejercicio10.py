n = int(input("Introduce un numero entero positivo mayor que 2: "))

for i in range(2, n):
    if n % 1 == 0:
        break
if (i + 1) == n:
    print(n, "es primo")
else:
    print(n, "no es primo")