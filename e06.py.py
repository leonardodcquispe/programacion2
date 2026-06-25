# Un cajero automático entrega solo billetes de $1000 y de $200.
# Ingresar la cantidad que desea extraer el usuario y luego indicar cuántos billetes de $1000 y de $200 se le entregan. 
# Además, indicar el saldo que no se pudo extraer porque no hay billetes. 

monto= int(input("Ingresa el monto a extraer: "))
mil= monto//1000
resto= monto%1000
doscientos= resto//200
noSaldo= resto%200
print("Se entregan ", mil, " billetes de $1000.")
print("Se entregan ", doscientos, " billetes de $200.")
print("Saldo no extraído: $", noSaldo)