def suma(num1, num2):
    return num1 + num2


def suma2(n1 : int, n2 : int) -> int: #DEf tipo de variable y 
    return n1 + n2                    #tabmbien el tipo a la funcion

def suma3(n1 : int = 0, n2 : int = 3) -> int: #se remplaza el 0
    return n1 + n2 
        
print(suma(5,8))
print(suma2(2,5))
print(suma3(1)) #solo si aqui pasamos un valor


#una variable global no se puede puede modificar en una funcion
#a menos que se use el comando global
def spam():
    global eggs  #Declarar que estamos modificando la variable global.
    eggs = 'spam'#Esto modifica la variable global.
eggs = 'global'
spam() #La función modifica la variable global.
print(eggs)
    