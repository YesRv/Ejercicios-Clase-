
lista = [1,2,3,4,25,45,56,78,89,90,106,234,345,456]
inicio = 0
final = len(lista) - 1
med = (inicio + final) // 2
buscador = False

## Debo tener dos punteros que recorreran mi lista INICIO Y FIN

n1 = int(input("Escribe: "))

##Mientras mi condicion sea falsa y mi inicio y final no se crucen, el bucle continuara con el resto de condiciones

while buscador == False and inicio<=final:
    ##Si el recorrido de mi lista es igual al numero que estoy buscando el codigo me muestra el número
    if lista[med] == n1:
        print ("Encontraste el numero",n1," En la posición ",med)
        buscador = True
    elif lista[med] > n1:
        inicio = med + 1
        med  = ((inicio + final) // 2) 
    else: 
        final = med - 1 
        med  = ((inicio + final) // 2) 

if not buscador:
    print("not found")


