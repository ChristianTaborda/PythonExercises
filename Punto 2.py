
A = int(input("Digite el primer número: "))
B = int(input("Digite el segundo número: "))

parcial = A + B

print("La suma es: " + str(parcial))

total = parcial

decision = str(input("¿Desea realizar otra suma (s/n)?: "))

while decision == "s":
    
    A = int(input("Digite el primer número: "))
    B = int(input("Digite el segundo número: "))

    parcial = A + B

    print("La suma es: " + str(parcial))

    total = total + parcial

    decision = str(input("¿Desea realizar otra suma (s/n)?: "))

print("La suma total de todos los números digitados es: " + str(total))
