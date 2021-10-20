#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
matriz = []
#salida = ""
ruta = str(input("Escribe la ruta del archivo .txt con las instrucciones en\n \
        ensamblador: "))
archivo= open(ruta,"r")
matriz_datos= archivo.read().rstrip().replace("\t","").split("\n")

lineas_ensamblador = len(matriz_datos)

for j in range (lineas_ensamblador):
    matriz.append([])
   # for i in range(lineas_ensamblador):
    matriz[j].extend(matriz_datos[j].split(","))
       # matriz.append([])

print (matriz_datos)
print ( "\n*********\n")
for j in range(lineas_ensamblador):
    print(matriz[j])


archivo.close()
#archivo_salida= open("./salida.txt","w")
#archivo_salida.write(salida)
#archivo_salida.close()
