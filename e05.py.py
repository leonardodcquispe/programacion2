# Un profe tiene X caramelos y los quiere repartir entre Y estudiantes; reciben un número entero de caramelos.
# Preguntar al usuario X e Y. Luego, indicar cuántos caramelos le tocan a cada estudiante y cuántos sobran en la bolsa.

caramelos= int(input("Ingresa el número de caramelos: "))
estudiantes = int(input("Ingresa el número de estudiantes: "))
division = caramelos // estudiantes
sobran = caramelos % estudiantes
print("A cada estudiante le corresponden ", division, " caramelos.")
print("Sobran ", sobran, " caramelos en la bolsa.")