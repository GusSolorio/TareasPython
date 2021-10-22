#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
resultado = []
matriz = []
auxiliar = []
valor_etiqueta= []
auxiliar2 = []
imm = []
relleno = "00000"
rellenojr = "00000000000"
######## Definicion de diccionarios ############
etiquetas= {}

oppcode = {'add':'0000','addi':'0001','and':'0010','andi':'0011','beq':'0100',\
        'bne':'0101','j':'0110', 'jal':'0111','jr':'1010','lb':'1011','or':'1100',\
        'sb':'1101','sll':'1110','srl':'1111' }
Rx={'x0':'000','x1':'001','x2':'010','x3':'011','x4':'100','x5':'101','x6':'110',\
'x7':'111','X0':'000','X1':'001','X2':'010','X3':'011','X4':'100','X5':'101',\
'X6':'110','X7':'111'}
###########################################

#############################################
""" Guarda el valor de la ruta, solo agregar el nombre del archivo ######
 tiene que estar en el mismo directorio                            """
ruta = str(input("Escribe la ruta del archivo .txt con las instrucciones en\n\
ensamblador: "))
ruta="./"+ruta
##############################################################

""" Abre el archivo y guarda los datos en un array
matriz_datos = [Linea 1 del txt, Linea 2 del txt, ...]"""
archivo= open(ruta,"r")
matriz_datos= archivo.read().strip().replace("\t","").replace(" ","").split("\n")

"""
***Busca etiquetas en caso de que existan, las guarda en un diccionario con su
***valor
"""
for j in range (len(matriz_datos)):
    if(":" in matriz_datos[j]):
        valor_etiqueta.append(j+1)
        auxiliar.extend(matriz_datos[j].split(":"))
        #etiquetas[auxiliar[j]] = valor_etiqueta[j]
        auxiliar2.append(auxiliar[j])
        del auxiliar[j]
    else:
        auxiliar.extend(matriz_datos[j].split(":"))
   # print(auxiliar[j])

for j in range (len(auxiliar2)):
    etiquetas[auxiliar2[j]]=valor_etiqueta[j]
"""
Diccionario etiquetas
"""
#print(etiquetas)
#print("****")


for j in range (len(matriz_datos)):
    matriz.append([])
    resultado.append([])
    matriz[j].extend(auxiliar[j].split(","))
    resultado[j].extend(auxiliar[j].split(","))

"""
"""
for j in range(len(matriz_datos)):
    imm.append(None)
    if (matriz[j][0] == "j") or (matriz[j][0]=="jal") or (matriz[j][0]== "jr"):
        imm[j]= None
    elif (matriz[j][3] == "x0")or(matriz[j][3] == "x1")or(matriz[j][3] =="x2")\
            or (matriz[j][3] == "x3") or (matriz[j][3] == "x4")or\
            (matriz[j][3] =="x5")or(matriz[j][3] == "x6")or(matriz[j][3] == "x7"):
        imm[j]= None
    elif (matriz[j][0]=="beq")or(matriz[j][0]=="bne"):
        imm[j] = None
    else:
        imm[j]= eval(matriz[j][3])

#imprime los valores en int de imm
print(imm)
for l in range (len(imm)):
    if (imm[l] != None):
        imm[l] = (bin(((1 << 8) -1) & imm[l])[2:]).zfill(8)
#imprime los valores en 8 bits de imm
print(imm)
print(etiquetas)

print("**matriz***")
for j in range (len(matriz_datos)):
    print(matriz[j])

"""          i
    matriz= [ ,  ,  , ] j
            [ ,  ,  , ]
            [ ,  ,  , ]
"""


for j in range (len(matriz_datos)):
    for i in range(len(matriz[j])):
        if i == 0:
            resultado[j][i] = oppcode[matriz[j][i]]
        elif i==1:
            if (matriz[j][0] == "j")or(matriz[j][0] == "jal"):
                if matriz[j][i] in etiquetas.keys():
                    tag = etiquetas[matriz[j][i]]
                else:
                    tag = eval(matriz[j][i])
                resultado[j][i] = (bin(((1<<14)-1)& tag)[2:]).zfill(14)
            elif (matriz[j][0] == "jr"):
                resultado[j][i] = Rx[matriz[j][i]] + rellenojr
            elif (matriz[j][0] == "bne") or (matriz[j][0] == "beq"):
                resultado[j][i] = Rx[matriz[j][i]]
            elif (matriz[j][0] == "sll")or (matriz[j][0] == "srl"):
                resultado[j][i] = Rx[matriz[j][i+2]]
            elif (matriz[j][0] == "sb") or (matriz[j][0] == "lb"):
                resultado[j][i] = Rx[matriz[j][i+2]]
            elif (matriz[j][0] == "addi")or(matriz[j][0]=="andi"):
                resultado[j][i] = Rx[matriz[j][i+1]]
            else:
                resultado[j][i] = Rx[matriz[j][i+1]]
        elif i==2:
            if (matriz[j][0] == "j")or(matriz[j][0] == "jal"):
                x="no hace nada"
            elif (matriz[j][0] == "jr"):
                x="no hace nada"
            elif (matriz[j][0] == "bne") or (matriz[j][0] == "beq"):
                resultado[j][i] = Rx[matriz[j][i]]
            elif (matriz[j][0] == "sll"):
                resultado[j][i] = Rx[matriz[j][i]]
            elif (matriz[j][0] == "srl"):
                resultado[j][i] = Rx[matriz[j][i-1]]
            elif (matriz[j][0] == "sb") or (matriz[j][0] == "lb"):
                resultado[j][i] = Rx[matriz[j][i-1]]
            elif (matriz[j][0] == "addi")or(matriz[j][0]=="andi"):
                resultado[j][i] = Rx[matriz[j][i-1]]
            else:
                resultado[j][i] = Rx[matriz[j][i+1]]
       #     matriz[j][i]=Rx[matriz[j][i]]
       # elif i== 2:
       #     matriz[j][i]=Rx[matriz[j][i]]

print("\n****resultado*****\n")
for j in range(len(matriz_datos)):
    print(resultado[j])

print("****matriz***")
for j in range(len(matriz_datos)):
    print(matriz[j])
archivo.close()
#archivo_salida= open("./salida.txt","w")
#archivo_salida.write(salida)
#archivo_salida.close()
