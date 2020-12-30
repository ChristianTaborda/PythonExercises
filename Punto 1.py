
print("############CALCULO DE SERIES############")
print("Para seleccionar el tipo de sucesión:")
print("1- Geométrica ó 2- Aritmética")

tipo = int(input("Escriba el tipo de sucesión que desea calcular: "))
inicio = int(input("Escriba el valor de inicio de la sucesión: "))
cantidad = int(input("Escriba la cantidad de dígitos de la sucesión: "))
crecimiento = int(input("Escriba el valor de crecimiento de la sucesión: "))

if(tipo == 1):
    print("El resultado de la sucesión geométrica es: ", end = "")
elif(tipo == 2):
    print("El resultado de la sucesión aritmética es: ", end = "")

for x in range (0,cantidad,1):

    print(str(inicio), end = " ")

    if(tipo == 1):
        inicio = inicio * crecimiento
    elif(tipo == 2):
        inicio = inicio + crecimiento
    

    
       
