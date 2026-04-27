#Agrega los números pares del 1 al 10.
lista = [ x for x in range(1, 10 +1)]
print(lista)    

# Agrega solo los números pares mayores o iguales a 12.
lista = [2 * x for x in range(1, 10 +1) if x * 2 >= 12] 
print(lista)

# multiplos de 3 del 1 al 100
lista2 = [x for x in range(1, 100+1) if x % 3 == 0]
print(lista2)