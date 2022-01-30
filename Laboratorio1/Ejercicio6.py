from cgi import print_directory


p=input("Imgrese su pero en kg ")
e=input("Ingrese su estatura en metros ")
imc=round(float(p)/float(e)**2,2)
print("Tu indice de masa corporal es ",imc)