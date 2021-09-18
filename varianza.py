#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
#
#*** Tarea 1 pseudocodigo para calcular la varianza de 5 numeros introducidos
#*** por el usuario
#
#*** Alumno: Gustavo Alejandro Solorio Ramos
#*** Correo: gustavo.solorio@iteso.mx
#
#   --- Se calcula con la formula
#
#          (x_1-promedio)² + (x_2-promedio)² + ... + (x_n-promedio)²
#   σ²=  -----------------------------------------------------------
#                                     N
#
#En este caso N = 5

#Se solicita al usuario que ingrese los 5 numeros uno por uno
numero1 = eval (input("Ingresa el numero 1: "))
numero2 = eval (input("Ingresa el numero 2: "))
numero3 = eval (input("Ingresa el numero 3: "))
numero4 = eval (input("Ingresa el numero 4: "))
numero5 = eval (input("Ingresa el numero 5: "))

#Se calcula el promedio de los datos introducidos, ya que acorde a la formula
#a emplear se resta a cada numero
promedio = (numero1 + numero2 + numero3 + numero4+ numero5)/5

#Se introduce de forma manual la formula, sustituyendo los datos mostrados 
#al inicio por las variables del programa
varianza = (((numero1 - promedio)**2) + ((numero2 - promedio)**2) + ((numero3 -
    promedio)**2) + ((numero4 - promedio)**2) + ((numero5 - promedio)**2))/5

#Se muestra la varianza obtenida para los datos introducidos
print("La varianza obtenida de los numeros es: ",varianza)
