
def descontar(V,D):

    return V - D

def obtenerDescuento(V,P):

    if(P == "20.0  %"):
        V = V * 0.2
    elif(P == "30.0  %"):
        V = V * 0.3
    elif(P == "80.0  %"):
        V = V * 0.8

    return V
    
def obtenerPorcentaje(P):

    if(P >= 4.7):
        salida = "80.0  %"
    elif(P >= 4.5 and P < 4.7):
        salida = "30.0  %"
    elif(P >= 4.3 and P < 4.5):
        salida = "20.0  %"

    return salida

def imprimirEstudiante(C,N,V,P,PJ,D,VD):

    print("============DATOS DEL ESTUDIANTE============")
    print("Código\t : " + str(C))
    print("Nombre\t : " + str(N))
    print("Promedio : " + str(P))

    print("\n")
    print("========== DATOS MATRICULA FINANCIERA =======")
    print("Valor Matrícula\t\t: " + str(V))
    print("Porcentaje a descontar  : " + PJ)
    print("Valor Descuento\t\t: " + str(D))
    print("Total a pagar\t\t: " + str(VD))
    
cantidad = int(input("Digite la cantidad de estudiantes: "))
plan = str(input("Digite el nombre del plan: "))

totalIngresos = 0
totalDescuentos = 0

for x in range (0,cantidad,1):

    print("\n")
    codigo = int(input("Digite el código del estudiante: "))
    nombre = str(input("Digite el nombre completo del estudiante: "))
    valor = float(input("Digite el valor a pagar por concepto de matrícula: "))
    
    totalIngresos = totalIngresos + valor
    
    promedio = float(input("Digite el promedio del estudiante: "))
    porcentaje = obtenerPorcentaje(promedio)
    descuento = obtenerDescuento(valor,porcentaje)

    totalDescuentos = totalDescuentos + descuento
    
    valorDescontado = descontar(valor,descuento)

    print("\n")

    imprimirEstudiante(codigo,nombre,valor,promedio,porcentaje,descuento,valorDescontado)

ingresosNetos = totalIngresos - totalDescuentos

print("\n")
print("============RESUMEN - MATRICULA FINANCIERA ==")
print("Plan\t: " + plan)
print("Total ingresos\t : " + str(totalIngresos))
print("Total descuentos : " + str(totalDescuentos))
print("Ingresos Netos\t : " + str(ingresosNetos))
