"""
            Serie de Fibonacci Recursiva
Si en el programa especificamos la cantidad de 11, nos debe mostrar lo siguiente:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
"""

def Fibonacci(numero):
    if(numero == 0 or numero == 1):
        return numero
    else:
        return Fibonacci(numero - 1) + Fibonacci(numero - 2)

#Vamos a Presentar un Total de 11 Numeros Fibonacci
#El usuario puede pedir que se ingrese la cantidad a querer iniciarse
cantidad = 11 #El valor es preferencia del usuario

#Si queremos presentar la serie lo hacemos por medio de un ciclo for
for i in range(cantidad):
    print(Fibonacci(i), end=" ") #el end sirve para mantenernos en la misma línea
