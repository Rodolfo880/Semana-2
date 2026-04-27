#Uso de if, elif (Elseif) y else
edad : int = 70
if edad == 18:
    print(f"Mayor de edad")
elif edad < 18:
    print("Niño")
else:
    print("Muy viejo")

#Ejemplo de While
sapam = 0
while sapam < 5:  
    print("Hola de nuevo")
    sapam = sapam + 1
    print() # espacio en blanco

#Algo parecido pero con for
for repet in range (5):  #[0,1,2,3,4]
    print(f"Se detiene en 5 o 4? {repet}")

#Otro ejemplo (1) de como se puede usar for avansa
for i in range (0,10, 2): # range(inicia desde 0,avanza asta 10, 2 en 2 
    print(f"Subida {i}")  
print()

#Ejemplo 2 con for retrocede
for a in range (2, -3, -1): #range(inicia en 2 retrocede asta -3, 1 en 1)
    print(f"Atras {a}")
