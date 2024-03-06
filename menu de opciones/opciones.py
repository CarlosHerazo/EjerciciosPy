import math
import matplotlib.pyplot as plt
import numpy as np
from colorama import init, Fore, Style


class Opciones:
    def __init__(self):
        self.vector = ["Julia", "Carlos", "Maria", "Ester", "Harold"]

    def invalido(self):
        print(Fore.RED + "Opcion no valida" + Style.RESET_ALL)

    def salir(self):
        print(Fore.YELLOW + "Gracias por Usar nuestro menú!!!" + Style.RESET_ALL)

    def mostrar_menu(self):
        init(autoreset=True)
        print(Fore.GREEN + Style.BRIGHT + "****************************************")
        print(
            Fore.GREEN
            + Style.BRIGHT
            + format("*           Menú de Opciones           *", "*^38")
        )
        print(Fore.GREEN + Style.BRIGHT + "****************************************")
        print(Fore.CYAN + Style.BRIGHT + "* 1. Sumar                             *")
        print(Fore.CYAN + Style.BRIGHT + "* 2. Restar                            *")
        print(Fore.CYAN + Style.BRIGHT + "* 3. Multiplicar                       *")
        print(Fore.CYAN + Style.BRIGHT + "* 4. Dividir                           *")
        print(Fore.CYAN + Style.BRIGHT + "* 5. Verificar el nombre del vector    *")
        print(Fore.CYAN + Style.BRIGHT + "* 6. Sumar dos matrices                *")
        print(Fore.CYAN + Style.BRIGHT + "* 7. Raiz cuadrada de un numero        *")
        print(Fore.CYAN + Style.BRIGHT + "* 8. Calcular el promedio de 3 notas   *")
        print(Fore.CYAN + Style.BRIGHT + "* 9. Graficar                          *")
        print(Fore.CYAN + Style.BRIGHT + "* 10. Salir                            *")
        print(Fore.GREEN + Style.BRIGHT + "****************************************")

    def sumar(self, num1, num2):
        resultado = num1 + num2
        return print("La sumatoria es: ", resultado)

    def restar(self, num1, num2):
        resultado = num1 - num2
        return print("La resta es: ", resultado)

    def multiplicar(self, num1, num2):
        resultado = num1 * num2
        return print("La multiplicacion es: ", resultado)

    def dividir(self, num1, num2):
        if num2 == 0:
            return print("No se puede dividir entre 0.")
        resultado = num1 / num2
        return print("La division es: ", resultado)

    def verificar_nombre(self, nombre):
        if nombre in self.vector:
            return print(f"El nombre {nombre} existe en el vector.")
        else:
            return print(f"El nombre {nombre} no existe en el vector.")

    def sumar_matrices(self, filas, columnas):

        print("Ingrese los elementos de la Matriz A (separados por espacio o coma): ")
        Matriz_A = []
        for _ in range(filas):
            fila = list(map(int, input().strip().split()))
            Matriz_A.append(fila)

        print("Ingrese los elementos de la matriz B (separados por espacio o coma):")
        Matriz_B = []
        for _ in range(filas):
            fila = list(map(int, input().strip().split()))
            Matriz_B.append(fila)

        # convertir las listas en matrices
        Matriz_A = np.array(Matriz_A)
        Matriz_B = np.array(Matriz_B)

        # realizar la suma de las matrices
        result_sumatoria = Matriz_A + Matriz_B

        print("La sumarotia de las dos matrices es: ")
        return print(result_sumatoria)

    def raiz_cuadrada(self, numero):
        resultado = math.sqrt(numero)
        return print(f"La raiz cuadrada de {numero} es {resultado}")

    def promedio_notas(self, nota1, nota2, nota3):
        resultado = np.mean(list([nota1, nota2, nota3]))
        return print(f"El promedio de calificacion es: {resultado} ")

    def graficar(self, datos):
        x = []
        y = []
        for _ in range(datos):
            year = int(input("Ingrese el año: "))
            x.append(year)

            people = int(input(f"Ingrese el total de personas para el año {year}: "))
            y.append(people)

        plt.plot(x, y, marker="o", linestyle="--", color="r")
        plt.xlabel("Años")
        plt.ylabel("Poblacion (M)")
        plt.title("Años vs Poblacion")
        plt.show()
