### Diccionario ejemplos 

colores = {"Rojo":"Red", "Verde": "Green", "Amarillo":"Yellow", "Rosa":"Pink", "Morado":"Purple"}
colores ["Naranja"] = "Orange" # Agrego en el diccionario que imprimo un nuevo valor al final 
del(colores["Verde"]) #Borro un elemento del diccionario



## Diccionarios dentro de un diccionario
hermanas = {"Yesica": {"Apellido": "Rodriguez", "Profesion": "Administradora", "Edad": 27}, 
   "Yuly":{"Apellido": "Buelvas", "Profesion": "Ingeniera", "Edad": 35},
   "Yuliana": {"Apellido": "Rodriguez", "Profesion": "Profesora", "Edad": 19}}

print (colores)
#get(clave, valor_por_defecto)
print(hermanas.get("Yesica", "No existe el registro")) # Trae un valor especifico, debo darle un mensaje default si no encuentro el valor 
print ("Yuly" in hermanas) # Devuelve un True o False si el valor buscado se encuentra en el diccionario o lista 
print(hermanas.keys()) #Muestra solo las claves
print(hermanas.values()) #Muestra solo los valores 




equipo = {10: "James Rodriguez", 7: "Luis Diaz", 20: "Juanfer Quintero", 12:"Camilo Vargas", 4:"Santiago Arias", 6:"Richard Ríos"}

## Muestra la cantidad de elementos dentro de un objeto
print (len(equipo))

## Convertir diccionario a lista con la funcion list y muestra las claves
claves = list(equipo)
print(claves)

# Convierto mi diccionario en una lista y accedo a su informacion a traves de las coordenadas 
items = list (equipo.items())
# Accedo a clave y valor dependiendo de la posicion del 'item' de mi 'lista'
print(items[1]) 
print(items[2])

print(items[0][1]) #Accedo al valor 
print(items[1][0]) #Accedo a la clave 
print (items[1][1]) # Aqui no se que paso

#Verifica si la clave existe dentro del diccionario 
if 10 in equipo:
    print ("Se encuentra en el diccionario")
else:
    print ("No se encuentra en el diccionario")
