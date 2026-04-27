"""
Haz un programa en Python que te muestre un menú con la primera opción 
que te permita crear una persona con nombre y DNI y la agregué a una lista de personas. 
El menú tendrá una segunda opción donde mostrará todas las personas. 
El menú tendrá una tercera opción que pedirá un DNI y eliminará a la persona con ese DNI.
"""
#Crear la clase Persona
class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def __str__(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}"
    
#Crear la lista de personas
lista_per = []

#Crear el menú
opc = 0  #Variable para almacenar la opción seleccionada por el usuario.
while opc != 9: #Mientras la opción no sea 9 (Salir), el menú seguirá mostrándose.
    #Solicita al usuario que ingrese una opción y la convierte a entero.
    opc = int(input("Seleccione una opcion: \n[1]CrearP \n[2]ListarP\n[3]EliminarP\n[9]Salir\n"))
   
    """Perimte crear una persona."""
    if opc == 1: 
        dni = input("Ingrese el DNI: ") #Ingrese el DNI
        nombre = input("Ingrese el nombre: ") #Ingrese el nombre
        nueva_P = Persona(nombre, dni) #Crea una nueva persona con los datos ingresados.
        lista_per.append(nueva_P) #Agrega la nueva persona a la lista de personas.

        """Permite mostrartodas las personas.""" 
    elif opc == 2:
        for persona in lista_per: #Toma cada persona en la lista de personas
            print(persona) #Imprime la información de cada persona.

        """Permite eliminar una persona por su DNI."""
    elif opc == 3:
        dniBo = input("ingrese el DNI a eliminar: ") #Ingrese el DNI a eliminar
        for indx,persona in enumerate(lista_per): #Toma cada persona en la lista de personas junto con su índice
            if persona.dni == dniBo: #Si el DNI de la persona coincide con el DNI ingresado para eliminar
                del lista_per[indx] #Elimina la persona de la lista utilizando su índice.
                print("Persona eliminada.") #Imprime un mensaje.
                break #Sale del bucle después de eliminar la persona.
        else:
            print("No se encontró la persona.")
            
    elif opc == 9:
        print("Saliendo del programa.")