#1. Funciones de uso recurrente

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese la opcion que desea utilizar: "))
            if opcion <= 0 or opcion >= 7:
                print("Opcion invalida - fuera de rango")
            else:
                return opcion
        except ValueError:
            print("Error - Dato invalido ingresado")

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por Plataforma")
    print("2. Busqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar Juego")
    print("5. Eliminar Juego")
    print("6. Salir")
    print("====================================")

#2. diccionarios paralelos

#Orden: [0] = Nombre del juego , [1] = Plataforma , [2] = genero , [3] = Clasificacion , [4] = Multiplayer (True/False) , [5] = Editor
juegos = { 
    'G001': ['Cyberpunk2077' , 'PC' , 'sandbox' , 'M' , False , 'CdProyectRed'],
    'G002': ['The Legend Of Zelda OT', 'Switch', 'aventura', 'E', False , 'Nintendo'],
    'G003': ['God of War 2018', 'PS5', 'aventura', 'M' , False , 'Santa Monica'],
    'G004': ['Halo Reach' , 'Xbox', 'accion', 'T' , True , 'Microsoft']
}



#Orden: [0] = Precio , [1] = Stock             ambos son enteros , solo el stock puede ser cero , el precio debe ser mayor a 0 

inventario = { 
    'G001': [28000, 4],
    'G002': [78000, 15],
    'G003': [49000, 7],
    'G004': [14990, 2],
}


#3. Funciones Tochas:

def stock_plataforma():
    plataforma = input("Que plataforma busca: ")
    encontrado = False
    stock_total = 0

    for codigo , datos in juegos.items():
        plataforma_actual = datos[1]
        if plataforma.upper().strip() == plataforma_actual.strip().upper():
            encontrado = True
            stock_total += inventario[codigo][1]
    
    if encontrado:
     print (f"La plataforma {plataforma} tiene en stock: {stock_total} juegos")
    else:
        print (f"No se encontro la plataforma: {plataforma}")












opcion = 0
while opcion !=6:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        stock_plataforma()
    
    elif opcion == 6:
        print("Saliendo del sistema . . . ")
        break
