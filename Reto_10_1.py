#Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

numeros_reales= []
suma = 0

cantidad_arreglo= int(input("¿De cuantos numeros quiere el arreglo de reales?:"))

primer_numero= float(input("Ingrese su primer numero para el arreglo de reales:"))
numeros_reales.append(primer_numero)
print(numeros_reales)#prueba
for i in range(cantidad_arreglo-2):
    numeros= float(input("Ingrese el siguiente numero: "))
    numeros_reales.append(numeros)
    print(numeros_reales)#prueba
ultimo_numero = float(input("Ingrese el ultimo numero para el arreglo:"))
numeros_reales.append(ultimo_numero)
print(numeros_reales)#prueba

for elemento in numeros_reales:
    suma += elemento
    print (suma)#prueba

promedio = suma / cantidad_arreglo

print("El promedio del arreglo de reales es:" + str(promedio))


