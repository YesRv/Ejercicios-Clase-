## Crear una matrix en la cual pida las dimensiones y pueda ingresar las variables que quiero


lista1 = ("A", "B", "C", "D", "E",
          "F", "G", "H", "I", "J", 
          "K", "L", "M", "N", "O")

lista2 = ()
n = int(input("Número de Filas: "))
m = int(input("Número de Columnas: "))

for i in range (1,n,1):
    for j in range (1,m,1):
        lista2[i][j] = input ("Ingrese una letra: ")
    
print ("\n Matriz ingresada")
for i in range (0,n,1):
    for j in range (0,m,1):
        print (lista2[i][j])
    print ()