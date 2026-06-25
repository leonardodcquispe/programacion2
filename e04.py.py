#  Una bacteria se reproduce en un lapso de una hora. Luego, por cada hora que pasa cada bacteria se reproduce en otra.
#  Preguntar al usuario cuántas horas pasaron e indicar cuántas bacterias habrá.

horas = int(input("Ingresa el número de horas: "))
bacterias = 2 ** horas
print("Hay ", bacterias, " bacterias despúes de ", horas, " horas")