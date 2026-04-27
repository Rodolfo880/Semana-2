class perro:
    #init constructor para un objeto.
    def __init__(self, _nombre = ""):
        self.nombre = _nombre
        self.edad = 1

    def __str__(self):
        return f"soy {self.nombre} y tengo {self.edad} años"

    def ladrar(self):
        return f"Guau, tengo {self.edad}"

fido = perro ("Fido")
print(fido) 