## Buscador diccionario 

contador = 3
seguir = "si"

coders = { 
          
    1: {"id":1025625447, 
        "Nombre":"Yesica", 
        "Apellido":"Rodriguez", 
        "Edad":27,
        "Nivel de ingles":"B2"
        },    
    2: {"id":5826987412, 
        "Nombre":"Maria", 
        "Apellido":"Muñoz", 
        "Edad":21,
        "Nivel de ingles":"B1"
        },
    3: {"id":3225457898, 
        "Nombre":"Jandy", 
        "Apellido":"Peña", 
        "Edad":21,
        "Nivel de ingles":"B1"
        },        
 }




while seguir == "si":
        print ("Coders")
        print ("1. Buscar elemento")
        print ("2. Agregar elemento")
        print ("3. Borrar elemento")
        print ("4. Salir")
        
        opcion = (input ("Escoge una opción: "))
        
        if opcion == "1":
            elemento = int (input ("Ingrese el número del elemento a buscar: "))
            print (coders.get(elemento, "No encontrado"))
        
        elif opcion == "2":
            contador += 1
            idCoder = int(input("Número de Id: "))
            nombreCoder = input ("Nombre Coder: ")
            apellidoCoder = input ("Apellido Coder: ")
            edadCoder = int(input("Edad coder: "))
            ingles = input ("Nivel de ingles: ")
            
            nuevoCoder = { "id":idCoder,
                          "Nombre":nombreCoder,
                          "Apellido": apellidoCoder,
                          "Edad":edadCoder,
                          "Nivel Ingles":ingles,    
                        }
            coders [contador] = nuevoCoder
            print (coders)
        elif opcion == "3":
            borrar = (int (input ("Ingrese el número del elemento que desea eliminar del diccionario: ")))
            del(coders[borrar])
            print (coders)
        elif opcion == "4":
            print ("Inventario Finalizado")
            seguir = "no"
          
        else:
            print ("Opción no valida intenta nuevamente")
                    
