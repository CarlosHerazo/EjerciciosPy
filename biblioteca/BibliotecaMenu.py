from Biblioteca import *


def mostrar_menu(user):
    print(f"===============================================")
    print(f"====== ADMINISTRACION BIBLIOTECARIA ===========")
    print(f"===============================================")
    print("= 1. Listar libros                            =")
    print("= 2. Agregar libro                            =")
    print("= 3. Salir                                    =")
    print(f"===============================================")


print("¡Bienvenido al Sistema Bibliotecario!")
usuario = input("Por favor, ingrese su nombre de usuario: ")


biblioteca = Biblioteca(usuario)

while True:
    mostrar_menu(usuario)
    opcion = input(f"{usuario}, selecciona una opcion (1-3): ")

    if opcion == "1":
        biblioteca._listarLibros()
    elif opcion == "2":
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        year = input("Ingrese el año de publicacion: ")
        editorial = input("Ingrese la editorial del libro: ")
        ref = input("Ingrese la referencia bibliografica: ")

        biblioteca._agregarLibros(titulo, autor, year, editorial, ref)
    elif opcion == "3":
        print(f"Hasta luego, {usuario}!")
        break
    else:
        print("Por favor, selecciona una opcion del 1 al 3")
