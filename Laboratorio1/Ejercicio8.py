c = float(input("Ingrese la cantidad a invertir "))
i = float(input("Ingrese la cantidad a invertir "))
a = int(input("Ingrese el numero de años "))
print("El capital obtenido es:",round(c * (i / 100 + 1) ** a, 2))