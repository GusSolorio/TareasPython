#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
#
#*** Tarea 2 pseudocodigo para calcular los valores de X_1,2 de una ecuacion
#*** Cuadrática introducida por el usuario
#
#*** Alumno: Gustavo Alejandro Solorio Ramos
#*** Correo: gustavo.solorio@iteso.mx
#
#   --- Se calcula con la formula
#
#          -b ±  sqrt(b²-4ac)
#   x_1,2=  -----------------
#                   2a
#
# Donde, de una ecuación cuadrática genérica, los valores son
#   Ax² + Bx + C = 0  || A, B y C puede ser cualquier numero real positivo
#   ^     ^    ^      ||          o negativo
#   a     b    c

#NO se ponen condiciones para cuando la Raiz cuadrada es imaginaria, por lo que
#El programa puede arrojar numeros complejos

#Se solicita al usuario que ingrese los valores A, B y C uno por uno siguiendo
#un ejemplo
print("Favor de escribir uno a uno los coeficientes A, B y C de la ecuacion\ncuadrática siguiendo el siguiente ejemplo\nAx² + Bx + C = 0\n")
CoeficienteA = eval (input("Ingresa el coeficiente A: "))
CoeficienteB = eval (input("Ingresa el coeficiente B: "))
CoeficienteC = eval (input("Ingresa el coeficiente C: "))

#Para simplificar la formula, se obtiene el valor de sqrt(b²-4ac)
Raiz = (CoeficienteB**2 - (4*CoeficienteA*CoeficienteC))**(1/2)

#Se calcula X_1 sumando el valor de la raiz cuadrada acorde a la formula
FormulaGeneral1 = ((-1)*CoeficienteB + Raiz)/(2*CoeficienteA)

#Se calcula X_2 restando el valor de la raiz cuadrada acorde a la formula
FormulaGeneral2 = ((-1)*CoeficienteB - Raiz)/(2*CoeficienteA)

#Se muestran los resultados para los que se resuelve la ecuación
print("La solucion es: \nX_1 =",FormulaGeneral1,"\nX_2 =",FormulaGeneral2)

