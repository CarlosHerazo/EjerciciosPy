import json  # importamos la libreria json


def leer(ruta):
    with open(ruta) as contenido:
        datos = json.load(contenido)  # load convierte a json lo pasado como parametro


        for _, val in datos.items():
            res = val[0]["cliente"]
            print(res)


ruta = "json/pizza.json"
leer(ruta)

"""Asi mandamos datos desde py a json """

datos = {"nombre": "Juan", "edad": 25, "ciudad": "Ejemploville"}

# Escribir datos en un archivo JSON
archivoDestino = "json/datos.json"
with open(archivoDestino, "w") as archivo:
    json.dump(datos, archivo)
    print(f"Datos guardados en {archivoDestino}")
