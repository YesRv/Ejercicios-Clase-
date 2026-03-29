## Empaquetar y desempaquetar
t1 = ("Rosa", 27, "Yesica", "Coder")

color, edad , nombre, profesion  = t1

#print (nombre) ## Desempaqueto un valor
#print (t1.index(27)) # Mostrar la posicion de una variable dentro de una tupla

t2 = ( "A", "B", "C", "B", "B", "B", "C", "C")
#print(t2.count("B")) # Cuenta cuantas veces esta una variable dentro de una tupla


t3 = ("A", "B", "C", "B", "B", "B", "C", "C", 56, 56, 25, 25, 25, 1, 2, 3)
i,*j,k = t3

#print (i,*j,k)

# Buscar Valores con matrices
t4 = (
        ("helado", 1500), 
        ("Bolis", 1200), 
        ("Raspao", 2500),
        ("Gaseosa", 3500)
        )
print ("El precio del" , t4[1][0] , "es: " , t4[1][1])


