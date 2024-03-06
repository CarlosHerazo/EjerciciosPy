from opciones import Opciones
import os

# instanciamos la clase opciones
opciones = Opciones()


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


opciones = Opciones()
while True:
    opciones.mostrar_menu()
    opcion_elegida = int(input("Ingrese el numero que deseada: "))

    if opcion_elegida == 1:
        print("Eligio la opcion para sumar: ")
        num1 = float(input("Ingrese el numero 1: "))
        num2 = float(input("Ingrese el numero 2: "))
        opciones.sumar(num1, num2)
        input("Presione Enter para continuar...")
        limpiar()
    elif opcion_elegida == 2:
        print("Eligio la opcion para restar: ")
        num1 = float(input("Ingrese el numero 1: "))
        num2 = float(input("Ingrese el numero 2: "))
        opciones.restar(num1, num2)
        input("Presione Enter para continuar...")
        limpiar()
    elif opcion_elegida == 3:
        print("Eligio la opcion para multiplicacion: ")
        num1 = float(input("Ingrese el numero 1: "))
        num2 = float(input("Ingrese el numero 2: "))
        opciones.multiplicar(num1, num2)
        limpiar()
        input("Presione Enter para continuar...")
    elif opcion_elegida == 4:
        print("Eligio la opcion para division: ")
        num1 = float(input("Ingrese el numero 1: "))
        num2 = float(input("Ingrese el numero 2: "))
        opciones.dividir(num1, num2)
        input("Presione Enter para continuar...")
        limpiar()
    elif opcion_elegida == 5:
        print("Ingrese su nombre para verificar: ")
        nombre = input("Ingresa el nombre: ")
        formatN = nombre.capitalize()
        opciones.verificar_nombre(formatN)
        input("Presione Enter para continuar...")
        limpiar()
    elif opcion_elegida == 6:
        matriz_Fil = int(input("Ingrese el numero de filas para la Matriz : "))
        matriz_Col = int(input("Ingrese el numero de columnas para la Matriz: "))
        opciones.sumar_matrices(matriz_Fil, matriz_Col)
        input("Presione Enter para continuar...")
    elif opcion_elegida == 7:
        numero = int(input("Ingresa un numero para hallar su raiz cuadrada: "))
        opciones.raiz_cuadrada(numero)
        input("Presione Enter para continuar...")
        limpiar()
    elif opcion_elegida == 8:
        nota1 = float(input("Ingrese su nota del primer corte: "))
        nota2 = float(input("Ingrese su nota del segundo corte: "))
        nota3 = float(input("Ingrese su nota del tercer corte: "))
        opciones.promedio_notas(nota1, nota2, nota3)
        input("Presione Enter para continuar...")
        limpiar()
    elif opcion_elegida == 9:
        datos = int(input("¿Cuantos datos desea ingresar?"))
        opciones.graficar(datos)
    elif opcion_elegida == 10:
        opciones.salir()
        break
    else:
        limpiar()
        opciones.invalido()
