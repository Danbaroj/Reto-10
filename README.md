## Reto-10

1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

```python
numeros_reales= [] # Inicializa una lista vacía para almacenar los números reales
suma = 0 # Inicializa la variable suma en 0 para acumular la suma de los números


cantidad_arreglo= int(input("¿De cuantos numeros quiere el arreglo de reales?:"))

primer_numero= float(input("Ingrese su primer numero para el arreglo de reales:"))
numeros_reales.append(primer_numero)

#Utiliza un bucle for para pedir al usuario los números intermedios

for i in range(cantidad_arreglo-2):

    numeros= float(input("Ingrese el siguiente numero: "))
    numeros_reales.append(numeros)

ultimo_numero = float(input("Ingrese el ultimo numero para el arreglo:"))
numeros_reales.append(ultimo_numero)

# Utiliza un bucle for para calcular la suma de todos los números en la lista

for elemento in numeros_reales:
    suma += elemento

# Calcula el promedio

promedio = suma / cantidad_arreglo

# Imprime el promedio del arreglo de números reales

print("El promedio del arreglo de reales es:" + str(promedio))
```

2. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

```python

# Inicialización de las listas para los dos arreglos y para el almacenamiento de los elementos resultantes de la multiplicacion de los dos arreglos

primer_arreglo = []
segundo_arreglo = []
producto_punto = []

# Variable para controlar la posición dentro de los arreglos

posicion_arreglo = 0

# Inicializa la variable suma en 0 para acumular la suma de los elementos resultantes luego de multiplicar entre los dos arreglos

suma = 0

tamaño_arreglos = int(input("Ingrese que tamaño van a tener los dos arreglos: "))

print("Agregue los numeros del primer arreglo")
print()

primer_num_arreglo_prim = int(input("Ingrese su primer numero para el primer arreglo:"))
primer_arreglo.append(primer_num_arreglo_prim)

# Utiliza un bucle for para pedir al usuario los números intermedios del primer arreglo

for i in range(tamaño_arreglos - 2):
    numeros_primer = int(input("Ingrese el siguiente numero: "))
    primer_arreglo.append(numeros_primer)

ultimo_num_arreglo_prim = int(input("Ingrese el ultimo numero para el arreglo:"))
primer_arreglo.append(ultimo_num_arreglo_prim)


print("Agregue los numeros del segundo arreglo")
print()


primer_num_arreglo_seg = int(input("Ingrese su primer numero para el primer arreglo:"))
segundo_arreglo.append(primer_num_arreglo_seg)

# Utiliza un bucle for para pedir al usuario los números intermedios del segundo arreglo

for i in range(tamaño_arreglos - 2):
    numeros_segund = int(input("Ingrese el siguiente numero: "))
    segundo_arreglo.append(numeros_segund)


ultimo_num_arreglo_seg = int(input("Ingrese el ultimo numero para el arreglo:"))
segundo_arreglo.append(ultimo_num_arreglo_seg)

# Calcula la multiplicación de cada elemento entre los dos arreglos

for numeros in primer_arreglo:
    numeros_lista = primer_arreglo[posicion_arreglo] * segundo_arreglo[posicion_arreglo]
    producto_punto.append(numeros_lista)  
    print(producto_punto)  
    posicion_arreglo += 1  

# Suma los elementos resultantes de multiplicar cada elemento entre los dos arreglos para obtener el resultado final del producto punto

for numero in producto_punto:
    suma += numero


print("El producto punto de el primer arreglo (" + str(primer_arreglo) + ") con el segundo arreglo (" + str(segundo_arreglo) + ") da como resultado: " + str(suma))
```

3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
```python
# Inicializa un arreglo vacío para almacenar los números
arreglo_numeros = []


cantidad_arreglo = int(input("¿De cuantos numeros quiere el arreglo?:"))

primer_numero = int(input("Ingrese su primer numero para el arreglo:"))
arreglo_numeros.append(primer_numero)

# Utiliza un bucle for para pedir al usuario los números intermedios
for i in range(cantidad_arreglo - 2):
    numeros = int(input("Ingrese el siguiente numero: "))
    arreglo_numeros.append(numeros)

ultimo_numero = int(input("Ingrese el ultimo numero para el arreglo:"))
arreglo_numeros.append(ultimo_numero)

# Imprime el arreglo de números original
print("Su arreglo de numeros es:" + str(arreglo_numeros))

# Recorre el arreglo de números
for numero in arreglo_numeros:
    # Si el número es 0, lo agrega al final del arreglo y lo elimina de su posición actual
    if numero == 0:
        arreglo_numeros.append(numero)
        arreglo_numeros.remove(numero)
    # Si el número no es 0, continúa con la siguiente iteración del bucle
    else:
        if numero != 0:
            continue

print("Su arreglo de numeros con los ceros al final del arreglo es:" + str(arreglo_numeros))
```
4. Revisar que son los algoritmos de sorting, entender bubble-sort (enlace a implementación).
Los algoritmos de soarting ponen orden en los elementos de un conjunto, ya sea de menor a mayor o viceversa. Algunos ejemplos comunes son Bubble Sort, Selection Sort e Insertion Sort, los cuales son fáciles de implementar pero lentos para conjuntos grandes.

Para conjuntos grandes, existen algoritmos más eficientes como Merge Sort, Quick Sort y Heap Sort, .

Elegir el algoritmo adecuado depende del tamaño del conjunto, la necesidad de estabilidad (mantener el orden relativo de elementos iguales) y la memoria disponible.

Bubble Sort: Un algoritmo simple que compara e intercambia elementos adyacentes si están en el orden incorrecto, como si "hiciera flotar" los elementos más grandes al final. Se repite este proceso hasta que la lista esté ordenada.
