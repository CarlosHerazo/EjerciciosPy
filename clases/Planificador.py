"""
Se requiere un planificador digital al mes, donde se pueda anexar actividades de acuerdo a
la agenda de una persona, este planificador deberá alertar al usuario de acuerdo a sus
actividades, teniendo en cuenta:
• Si ese día del mes es festivo;
• Si ese día del mes ya tiene un compromiso (laboral o recreativa)
• Deberá mostrar al usuario que días tiene ocupado y que días tiene desocupados del
mes.
Nota: Para realizar el planificador, deberá tener en cuenta el calendario
colombiano con sus festivos 2024.
"""

import calendar as cal
from colorama import Fore, Style
import os


class CalendarioP:
    def __init__(self, year, mes):
        self.year = year
        self.month = mes
        self.agenda = {}
        self.festivos = {"4": "Todos los santos", "11": "Independencia de Cartagena"}

    def mostrar_calendario(self):
        print(f"{Fore.CYAN}CALENDARIO{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}LU MA MI JU VI SA DO{Style.RESET_ALL}")

        # Obtener el calendario del mes
        month_calendar = cal.monthcalendar(self.year, self.month)

        for semana in month_calendar:
            for dia in semana:
                if dia == 0:
                    print("  ", end=" ")  # DIAS NO PERTENECIENTES AL MES
                else:
                    # COLOR A LOS DIAS FESTIVOS
                    if str(dia) in self.festivos:
                        print(f"{Fore.YELLOW}{dia:2}{Style.RESET_ALL}", end=" ")
                    elif str(dia) in self.agenda:
                        # COLOR A LOS DIAS NO FESTIVOS
                        print(f"{Fore.GREEN}{dia:2}{Style.RESET_ALL}", end=" ")
                    else:
                        print(f"{dia:2}", end=" ")
            print()

    def agregar_actividad(self, dia, actividad):
        if dia in self.agenda:
            print(
                f"{Fore.GREEN}El {dia}  {Style.RESET_ALL} ya esta ocupado con la actividad:{Fore.YELLOW} {self.agenda[dia]}{Style.RESET_ALL}"
            )
        else:
            self.agenda[dia] = actividad
            print(f"Actividad agregada para el dia {dia}: {actividad}")

    def mostrar_festivos(self):
        print(f"{Fore.YELLOW}DIAS FESTIVOS: {Style.RESET_ALL}")
        for fes in self.festivos:
            print(f"{Fore.YELLOW} {fes} {Style.RESET_ALL} : {self.festivos[fes]} ")

    def mostrar_agenda(self):
        self.mostrar_calendario()

        print(f"{Fore.GREEN}DIAS AGENDADOS: {Style.RESET_ALL}")
        for agen in self.agenda:
            print(f"{Fore.GREEN} {agen} {Style.RESET_ALL}: {self.agenda[agen]}")

    def eliminar_agenda(self):
        print(f"{Fore.RED}AGENDAMIENTOS PARA ELIMINAR: {Style.RESET_ALL}")
        for agen in self.agenda:
            print(f"{Fore.GREEN} {agen} {Style.RESET_ALL}: {self.agenda[agen]}")
        dia_E = input(
            f"{Fore.YELLOW}Por favor elige el dia a eliminar o precione 'Enter' para salir: {Style.RESET_ALL}"
        )
        if dia_E in self.agenda:
            print(
                f" El dia {Fore.GREEN}{dia_E}{Style.RESET_ALL} Fue removido con la actividad:{Fore.YELLOW} {self.agenda[dia_E]}{Style.RESET_ALL}"
            )
            self.agenda.pop(dia_E)

    def modificar_agenda(self):
        print(f"{Fore.RED}AGENDAMIENTOS PARA MODIFICAR: {Style.RESET_ALL}")
        for agen in self.agenda:
            print(f"{Fore.GREEN} {agen} {Style.RESET_ALL}: {self.agenda[agen]}")
        
            dia_E = input(
                f"{Fore.YELLOW}Por favor seleccione el dia a modificar o precione 'Enter' para salir: {Style.RESET_ALL}"
            )
        

        if dia_E in self.agenda:
            self.agenda[dia_E] = input("Por favor ingrese la nueva actividad: ")
            print(
                f" El dia {Fore.GREEN}{dia_E}{Style.RESET_ALL} Fue cambiado con la actividad:{Fore.YELLOW} {self.agenda[dia_E]}{Style.RESET_ALL}"
            )


agenda = CalendarioP(2024, 11)

while True:
    print("******************************")
    print("*   PLANIFICADOR DE TAREAS   *")
    print("******************************")
    print("* 1 Agregar plan             *")
    print("* 2 Mostrar festivos         *")
    print("* 3 Mostrar agenda           *")
    print("* 4 Eliminar agendamiento    *")
    print("* 5 Modificar agendamiento   *")
    print("* 6 Salir                    *")
    print("******************************")
    print()

    op = input("Ingrese una opcion: ")
    if op == "1":
        os.system("cls")
        print("AGREGAR PLAN")
        agenda.mostrar_calendario()
        dia = input("Ingresa el dia para la agenda: ")
        actividad = input("Ingresa la actividad: ")
        agenda.agregar_actividad(dia, actividad)
        input("Enter para continuar...")
        os.system("cls")
    elif op == "2":
        agenda.mostrar_festivos()
        input("Enter para continuar...")
        os.system("cls")
    elif op == "3":
        agenda.mostrar_agenda()
        input("Enter para continuar...")
        os.system("cls")
    elif op == "4":
        agenda.eliminar_agenda()
        input("Enter para continuar...")
        os.system("cls")
    elif op == "5":
        agenda.modificar_agenda()
        input("Enter para continuar...")
        os.system("cls")
    elif op == "6":
        print("Saliendo de la agenda")
        break
    else:
        print("Opcion no valida")
