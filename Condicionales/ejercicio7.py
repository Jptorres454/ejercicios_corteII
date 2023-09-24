renta = float(input("Cual es tu valor en tu renta actual: "))

if renta <= 10000:
    print("Se te va otorgar un 5%")
    resultado = renta * 0.05
    print(f"Tu renta Se le otorgo un 5% de impositico: {resultado}€")
elif renta >= 10000 and renta <= 20000:
    print("Se te va otorgar un 15%")
    resultado = renta * 0.15
    print(f"Tu renta Se le otorgo un 15% de impositico: {resultado}€")
elif renta >= 20000 and renta <= 35000:
    print("Se te va otorgar un 20%")
    resultado = renta * 0.20
    print(f"Tu renta Se le otorgo un 20% de impositico: {resultado}€")
elif renta >= 35000 and renta <= 60000:
    print("Se te va otorgar un 30%")
    resultado = renta * 0.30
    print(f"Tu renta Se le otorgo un 30% de impositico: {resultado}€")
elif renta >= 60000:
    print("Se te va otorgar un 45%")
    resultado = renta * 0.45
    print(f"Tu renta Se le otorgo un 45% de impositico: {resultado}€")