#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
matriz = []

oppcode = {'add':'0000','addi':'0001','and':'0010','andi':'0011','beq':'0100',\
        'bne':'0101','j':'0110', 'jal':'0111','jr':'1010','lb':'1011','or':'1100',\
        'sb':'1101','sll':'1110','srl':'1111' }
Rt ={'x0':'000','x1':'001','x2':'010','x3':'011','x4':'100','x5':'101','x6':'110',\
'x7':'111','X0':'000','X1':'001','X2':'010','X3':'011','X4':'100','X5':'101',\
'X6':'110','X7':'111'}
#salida = ""
Rs = {'x0':'000','x1':'001','x2':'010','x3':'011','x4':'100','x5':'101','x6':'110',\
'x7':'111','X0':'000','X1':'001','X2':'010','X3':'011','X4':'100','X5':'101',\
'X6':'110','X7':'111'}
ruta = str(input("Escribe la ruta del archivo .txt con las instrucciones en\n\
ensamblador: "))
ruta="./"+ruta
archivo= open(ruta,"r")
matriz_datos= archivo.read().rstrip().replace("\t","").split("\n")

#lineas_ensamblador = len(matriz_datos)

for j in range (len(matriz_datos)):
    matriz.append([])
   # for i in range(lineas_ensamblador):
    matriz[j].extend(matriz_datos[j].split(","))
       # matriz.append([])
for j in range (len(matriz_datos)):
    for i in range(len(matriz[j])):
        if i == 0:
            matriz[j][i]=oppcode[matriz[j][i]]
        elif i == 1:
            matriz[j][i]=Rt[matriz[j][i]]
        elif i== 2:
            matriz[j][i]=Rs[matriz[j][i]]


print (matriz)
print ( "\n*********\n")
for j in range(len(matriz_datos)):
    print(matriz[j])

#print (oppcode[matriz[0][0]])


archivo.close()
#archivo_salida= open("./salida.txt","w")
#archivo_salida.write(salida)
#archivo_salida.close()
