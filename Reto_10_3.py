#Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

arreglo_numeros = []

cantidad_arreglo= int(input("¿De cuantos numeros quiere el arreglo?:"))

primer_numero= int(input("Ingrese su primer numero para el arreglo:"))
arreglo_numeros.append(primer_numero)

#Utiliza un bucle for para pedir al usuario los números intermedios



for i in range(cantidad_arreglo-2):

    numeros= int(input("Ingrese el siguiente numero: "))
    arreglo_numeros.append(numeros)

ultimo_numero = int(input("Ingrese el ultimo numero para el arreglo:"))
arreglo_numeros.append(ultimo_numero)

print("Su arreglo de numeros es:" + str(arreglo_numeros))

for numero in arreglo_numeros:
    if numero == 0:
        arreglo_numeros.append(numero)
        arreglo_numeros.remove(numero)
    else:
        if numero != 0:
            continue


print("Su arreglo de numeros con los ceros al final del arreglo es:" + str(arreglo_numeros))