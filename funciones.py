#ARATH EMMANUEL SANCHEZ ANDRADE 2025792 GRUPO 32
# VARIABLES
lista = []
id = 0

#FUNCIONES

def registrar():
    titulo_t = input("titulo del libro: ")
    autor_t = input("autor del libro: ")
    genero_t = input("genero del libro: ")
    año_de_publicacion_t = input("año de publicacion del libro: ")
    isbn_t = input("ISBN del libro: ")
    fecha_de_adquisicion_t = input("fecha de adquisicion del libro: ")

    libro = dict(id= nuevo_id(), titulo = titulo_t.upper(), autor = autor_t.upper(), genero = genero_t.upper(), año_de_publicacion = año_de_publicacion_t.upper(), isbn = isbn_t.upper(), fecha_de_adquisicion = fecha_de_adquisicion_t.upper())
    
    lista.append(libro)

def catalogo_completo():
    print("ID\tTITULO\tAUTOR\tGENERO\tAÑO DE PUBLICACION\tISBN\tFECHA DE ADQUISICION")

    for libro in lista:
        print(libro["id"],"\t",libro["titulo"],"\t",libro["autor"],"\t",libro["genero"],"\t",libro["año_de_publicacion"],"\t",libro["isbn"],"\t",libro["fecha_de_adquisicion"])
    print()

def reporte_autor():
    autores = set()
    for libro in lista:
        autores.add(libro["autor"])
    print("autores:")
    for autor in autores:
        print(autor)

    buscar = input("qué autor quieres buscar?")
    print("ID\tTITULO\tAUTOR\tGENERO\tAÑO DE PUBLICACION\tISBN\tFECHA DE ADQUISICION")

    for libro in lista:
        if libro["autor"] == buscar.upper():  
            print(libro["id"],"\t",libro["titulo"],"\t",libro["autor"],"\t",libro["genero"],"\t",libro["año_de_publicacion"],"\t",libro["isbn"],"\t",libro["fecha_de_adquisicion"])
    print()

def reporte_genero():
    generos = set()
    for libro in lista:
        generos.add(libro["genero"])
    print("generos:")
    for genero in generos:
        print(genero)

    buscar = input("qué genero quieres buscar?")
    print("ID\tTITULO\tAUTOR\tGENERO\tAÑO DE PUBLICACION\tISBN\tFECHA DE ADQUISICION")

    for libro in lista:
        if libro["genero"] == buscar.upper():  
            print(libro["id"],"\t",libro["titulo"],"\t",libro["autor"],"\t",libro["genero"],"\t",libro["año_de_publicacion"],"\t",libro["isbn"],"\t",libro["fecha_de_adquisicion"])
    print()

def reporte_año():
    buscar = input("qué año quieres buscar?")
    print("ID\tTITULO\tAUTOR\tGENERO\tAÑO DE PUBLICACION\tISBN\tFECHA DE ADQUISICION")

    for libro in lista:
        if libro["año_de_publicacion"] == buscar.upper():  
            print(libro["id"],"\t",libro["titulo"],"\t",libro["autor"],"\t",libro["genero"],"\t",libro["año_de_publicacion"],"\t",libro["isbn"],"\t",libro["fecha_de_adquisicion"])
    print()

def reporte_titulo():
    titulos = set()
    for libro in lista:
        titulos.add(libro["titulo"])
    print("titulos:")
    for titulo in titulos:
        print(titulo)

    buscar = input("qué titulo quieres buscar?")
    

    for libro in lista:
        if libro["titulo"] == buscar.upper():  
            print("id:\t", libro["id"])
            print("titulo:\t",libro["titulo"])
            print("autor:\t",libro["autor"])
            print("genero:\t",libro["genero"])
            print("año_de_publicacion:\t",libro["año_de_publicacion"])
            print("isbn:\t",libro["isbn"])
            print("fecha_de_adquisicion:\t",libro["fecha_de_adquisicion"])
    print()

def reporte_isbn():
    buscar = input("qué ISBN quieres buscar?")

    for libro in lista:
        if libro["isbn"] == buscar.upper():  
            print("id:\t", libro["id"])
            print("titulo:\t",libro["titulo"])
            print("autor:\t",libro["autor"])
            print("genero:\t",libro["genero"])
            print("año_de_publicacion:\t",libro["año_de_publicacion"])
            print("isbn:\t",libro["isbn"])
            print("fecha_de_adquisicion:\t",libro["fecha_de_adquisicion"]) 
    print()

def nuevo_id():
    global id
    id = id + 1
    return id





