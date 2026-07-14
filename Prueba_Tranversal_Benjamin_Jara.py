
#0. Funciones de validacion y busqueda


def validar_precio(precio):
    try:
        precio_corregido = int(precio)
        if precio_corregido <= 0 :
            print("Error - El precio ingresado no puede ser 0 o menor")
            return False
        else:
            return True
    except ValueError:
        print("Error - Dato invalido (Solo son validos enteros)")
        return False

def validar_texto(texto):
    texto_corregido = texto.strip()
    if texto_corregido == "":
        print("Error - No se puede ingresar un texto vacio")
        return False
    else:
        return True

def validar_clasificacion(clasificacion):
    clasificacion_corregida = clasificacion.strip().upper()
    if clasificacion_corregida == ("E" , "T" , "M"):
        return True
    else:
        print ("Clasificiacion invalida")
        return False

def validar_stock(stock):
    try:
        stock_corregido = int(stock)
        if stock_corregido <0 :
            print("Error - El stock ingresado no puede ser menor a 0")
            return False
        else:
            return True
    except ValueError:
        print("Error - Dato invalido (Solo son validos enteros)")
        return False

def validar_multiplayer(multiplayer):
    multiplayer_corregido = multiplayer.strip().lower()
    if multiplayer_corregido == ("s" , "n"):
        return True
    print("Multiplayer invalido")
    return False



def buscar_codigo(codigo_buscado):
    for codigo in juegos:
        codigo_actual = codigo
        if codigo_buscado == codigo_actual.upper().strip():
            return True
    
    return False



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


#3. Funcion de stock por plataforma:

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


#4. Funcion de busqueda por rango de precio

def busqueda_precio(p_min , p_max):
    encontrado = False
    juegos_encontrados = []


    for codigo , datos in inventario.items():
        precio = datos[0]
        if p_min <= precio <= p_max and inventario[codigo][1] > 0:
            encontrado = True
            juego = juegos[codigo][0]
            code = codigo

            nuevo_juego = {'Juego': juego , 'codigo': code }

            juegos_encontrados.append(nuevo_juego)

    if encontrado:
        print("Los juegos encontrados son:")
        print (juegos_encontrados) # ARREGLAR DESPUES !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    else:
        print ("No se encontraron juegos en ese rango de precio")



def actualizar_precio(codigo , nuevo_precio):
    print ("No")



def agregar_Juego(codigo , titulo , plataforma , genero , clasificacion , multiplayer , editor , precio , stock ):

    juegos[codigo: titulo , plataforma , genero , clasificacion , multiplayer , editor ]

    inventario[codigo: , int(precio) , int(stock)]

    print ("Se agrego el juego")

    return juegos , inventario















opcion = 0
while opcion !=6:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        stock_plataforma()
    elif opcion == 2:
        while True:
         print ("=== Busqueda de juegos por rango de precio === ")
         print ("-" * 20)

         p_min = input("Ingrese el precio minimo: ")
         p_max = input("Ingrese el precio maximo: ")

         if validar_precio(p_min) and validar_precio(p_max):
            p_min = int(p_min)
            p_max = int(p_max)
            if p_min > p_max:
                print ("El precio minimo no puede ser mayor al maximo")
                continue
            else:
                break
         else:
             continue
        
        busqueda_precio(p_min , p_max)
    
    elif opcion ==3:
        while True:
            codigo = input("Ingrese el codigo del juego: ").upper().strip()
            if buscar_codigo(codigo):
             nuevo_precio = input("Ingrese nuevo precio: ")
             if validar_precio(nuevo_precio):
                actualizar_precio(codigo , nuevo_precio)
                break
            else:
                continuar = input("Desea actualizar otro precio (s/n)?: ").lower().strip()
                if continuar == "s":
                    continue
                else:
                    break
    
    elif opcion ==4:
        codigo = input("Ingrese el nuevo codigo: ")
        #Datos que van en juegos

        titulo = input("Ingrese el titulo del juego: ")
        plataforma = input("Ingrese la plataforma del juego: ")
        genero = input("Ingrese el genero del juego: ")
        clasificacion = input("Ingrese la clasificacion del juego: ")
        multiplayer = input("El juego tiene multiplayer?: ")
        editor = input ("Ingrese el editor del juego: ")

        #Datos que van en inventario
        precio = input("Ingrese el precio del juego: ")
        stock = input("Ingrese el stock del juego: ")

        if buscar_codigo(codigo) == False and validar_texto(multiplayer) and validar_clasificacion(clasificacion) and validar_texto(titulo) and validar_texto(plataforma) and validar_texto(genero) and validar_texto(editor) and validar_precio(precio) and validar_stock(stock):
            if multiplayer == "s" :
                multiplayer = True
            else:
                multiplayer = False

            print("Agregando")
            
            agregar_Juego(codigo , titulo , plataforma , genero , clasificacion , multiplayer , editor , precio , stock )
        
        else:
            print ("Dato invalido")


    
        
    elif opcion == 6:
        print("Saliendo del sistema . . . ")
        break

























    #elif opcion == 7:
        codigo_buscado = input("Ingrese un codigo: ").upper().strip()

        if buscar_codigo(codigo_buscado):
            print("Codigo existente")
        else:
            print("Codigo no existe")