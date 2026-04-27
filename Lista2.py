def separaEnteroDecimal(n : float):
    return int(n), n - int(n)

lista = [7, 3, 5, 2, 8, 3]
print(len(lista)) # Cantidad de elementos.

#Agregar elementos a la lista
lista.append(9) # Agrega el número 9 al final de la lista.
print(lista)

#insertar valor  en una posición específica
lista.insert(1,8) # Agrega el número 8 en el indice 1.
print(lista)

#Quitar un elemento de la lista
del lista[2] # Elimina el elemento en el índice 2.
print(lista)
#----------------------------------------------------
lista.remove(5) # Elimina la primera aparición del número 5.
print(lista)
#----------------------------------------------------
lista.pop() # Elimina el último elemento de la lista.
print(lista)

#para saber el indice de un elemento
print(lista.index(3)) # Devuelve el índice del numero 5.

lista [0] = 0 # Cambia el valor del índice 0 a 0.
print(lista)

#Valores múltiples
a = 10
b = 20
c, d = a, b
print(f"c: {c}, d: {d}")

a, b = b, a
print(f"a: {a}, b: {b}")

print(separaEnteroDecimal(3.9))

print(1.77 in lista) #Busca un elemento en la lista f o v.