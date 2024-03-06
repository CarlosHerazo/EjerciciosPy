"""
En una prueba de salto de longitud, un atleta, después de realizar 5 saltos, ha conseguido
estas marcas:

salto 1 = 6,701m
salto 2 = 7,029m
salto 3 = 7,25m
salto 4 = 7m
salto 5 = 7,05m

Ordena los saltos de menor a mayor y calcula la media de todos sus saltos 

"""


class CalculoSaltos:
    def __init__(self, lista):
        self.lista = lista

    def _OrganizarSaltos(self):

        for i in range(len(self.lista) - 1):  # 2 - 1

            for j in range(0, len(self.lista) - i - 1):  # 0 , 1
                if self.lista[j] > self.lista[j + 1]:  # [12] > [10]
                    self.lista[j], self.lista[j + 1] = self.lista[j + 1], self.lista[j] # [10] [12]

        return self.lista

    def media(self):
        return sum(self.lista) / len(self.lista)
    


listaSaltos = []
while True:
    num = input("¿Cuantos saltos desea ingresar?: ")
    if num.isnumeric():
        numInt = int(num)
        break
    else:
        print("Ingrese un dato valido")

try:
    for saltos in range(1, numInt + 1):
        dig = float(input(f"Ingrese el salto {saltos}: "))
        listaSaltos.append(dig)

    calcular = CalculoSaltos(listaSaltos)
    res1 = calcular._OrganizarSaltos()
    res2 = calcular.media()
    
    print("Saltos Ordenados: ", res1)
    print("Media de Saltos: ", res2)
except:
    print("A pasado un error al momento de ingresar los valores")
