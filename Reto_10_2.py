primer_arreglo=[]
segundo_arreglo=[]
producto_punto=[]

posicion_arreglo=0

suma= 0

tamaño_arreglos = int(input("Ingrese que tamaño van a tener los dos arreglos: "))

print("Agregue los numeros del primer arreglo")

print()

primer_num_arreglo_prim= int(input("Ingrese su primer numero para el primer arreglo:"))
primer_arreglo.append(primer_num_arreglo_prim)

#Utiliza un bucle for para pedir al usuario los números intermedios

for i in range(tamaño_arreglos-2):

    numeros_primer= int(input("Ingrese el siguiente numero: "))
    primer_arreglo.append(numeros_primer)

ultimo_num_arreglo_prim = int(input("Ingrese el ultimo numero para el arreglo:"))
primer_arreglo.append(ultimo_num_arreglo_prim)

print("Agregue los numeros del segundo arreglo")

print()

primer_num_arreglo_seg= int(input("Ingrese su primer numero para el primer arreglo:"))
segundo_arreglo.append(primer_num_arreglo_seg)

#Utiliza un bucle for para pedir al usuario los números intermedios

for i in range(tamaño_arreglos-2):

    numeros_segund= int(input("Ingrese el siguiente numero: "))
    segundo_arreglo.append(numeros_segund)

ultimo_num_arreglo_seg = int(input("Ingrese el ultimo numero para el arreglo:"))
segundo_arreglo.append(ultimo_num_arreglo_seg)

print(primer_arreglo)
print(segundo_arreglo)

for numeros in primer_arreglo:
    numeros_lista = primer_arreglo[posicion_arreglo] * segundo_arreglo[posicion_arreglo]
    producto_punto.append(numeros_lista)
    print(producto_punto)
    posicion_arreglo += 1

for numero in producto_punto:
    suma += numero

print("El producto punto de el primer arreglo (" + str(primer_arreglo)+ ") con el segundo arreglo (" + str(segundo_arreglo) + ") da como resultado: " + str(suma) )