edad : int = 15
altura : float = 1.46
nombre : str = "Ara"
apellido = 'Terrones'
esLinda : bool = True
esDeCabello = False

print (f"{nombre} {apellido} tiene {edad} años y su carita {"es muy " if esLinda else "No es"}linda")

print (f"{nombre} es bajita {altura} cm, tiene el cabello {"largo" if esDeCabello else "corto"}")