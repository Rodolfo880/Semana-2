lista = ["lenoel",20,1.77,True]

print(lista[0]) #Imprime el que esta en la pocicion 0
print(lista[2]) #Imprime el que esta en la pocicion 2

#inicio con el final conectados
#formas para llegar al utimo elemento de la lista
print(lista[len(lista)-1])
print(lista[-1])
print()

#Extrer una parte de la lista
print(lista[1:3]) # 1 hasta el índice 2 (3 no incluido)
print(lista[:3]) # desde el inicio hasta el índice 2 
print(lista[2:]) # desde el índice 2 hasta el final
print(lista[:]) # toda la lista