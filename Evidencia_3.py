#ARATH EMMANUEL SANCHEZ ANDRADE 2025792 GRUPO 32
from Evidencia_3_funciones import *
#from Evidencia_3_autor import *
#from Evidencia_3_genero import *


leer_datos()

while True:
    print("Menú principal:")
    print("1. Registrar nuevo ejemplar")
    print("2. Consultas y reportes")
    print("3. Registrar autor")
    print("4. Registrar generos")
    print("0. Salir")


    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Has elegido la opción 1")
        registrar_ejemplar() #REGISTRAR NUEVO EJEMPLAR

    elif opcion == "3":
        print("Has elegido la opcion 3")
        registrar_autor()

    elif opcion == "4":
        print("Has elegido la opcion 4")
        registrar_genero()

    elif opcion == "2":
        print("Has elegido la opción 2")
        while True:
            print("Menú de consultas y reportes:")
            print("1. Consulta de titulo")
            print("2. Reportes")
            print("0. Volver al menú principal")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                print("Has elegido la opción 1") 
                while True:
                    print("Menú de consulta de titulo:")
                    print("1. Consulta por titulo")
                    print("2. Consulta por ISBN")
                    print("0. Volver al menú de consultas y reportes")

                    opcion = input("Elige una opción: ")

                    if opcion == "1":
                        print("Has elegido la opción 1") 
                        reporte_titulo() #CONSULTA POR TITULO
                    
                    elif opcion == "2":
                        print("Has elegido la opción 2")
                        reporte_isbn() #CONSULTA POR ISBN

                    elif opcion == "0":
                        print("Regresando al menú anterior...")
                        break
                    else:
                        print("Opción no válida. Por favor, elige de nuevo.")

            elif opcion == "2":
                print("Has elegido la opción 2")
                while True:
                    print("Menú de reportes:")
                    print("1. Catalogo completo")
                    print("2. Reporte por autor")
                    print("3. Reporte por genero")
                    print("4. Reporte por año de publicacion")
                    print("0. Volver al menú de consultas y reportes")

                    opcion = input("Elige una opción: ")

                    if opcion == "1":
                        print("Has elegido la opción 1")
                        catalogo_completo() #CATALOGO COMPLETO 
                    elif opcion == "2":
                        print("Has elegido la opción 2")
                        reporte_autor() #REPORTE POR AUTOR
                    elif opcion == "3":
                        print("has elegido la opción 3")
                        reporte_genero() #REPORTE POR GENERO
                    elif opcion == "4":
                        print("has elegido la opción 4")
                        reporte_año() #REPORTE POR AÑO DE PUBLICACION
                    elif opcion == "0":
                        print("Regresando al menú anterior...")
                        break
                    else:
                        print("Opción no válida. Por favor, elige de nuevo.")

            elif opcion == "0":
                print("Regresando al menú anterior...")
                break
            else:
                print("Opción no válida. Por favor, elige de nuevo.")



    elif opcion == "0":
        print("Saliendo del programa...")
        guardar_datos()
        break
    else:
        print("Opción no válida. Por favor, elige de nuevo.")
