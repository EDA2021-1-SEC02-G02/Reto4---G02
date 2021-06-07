"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


#_________________________________________________
connections = 'connections.csv'
countries = 'countries.csv'
lpoints = 'landing_points.csv'
#_________________________________________________

def printMenu():
    print("\n")
    print("Bienvenido")
    print("********************************************")
    print("Bienvenido")
    print("1- Cargar base de datos.")
    print("2- Req. 1.  Cantidad de Clusteres y verificacion de pertenencia: ")
    print("3- Req. 2.  Hallar Landing Points")
    print("4- Req. 3.  Ruta minima en distancia que conecta dos paises")
    print("5- Req. 4.  Red de expansion minima")
    print("6- Req. 5.  Impacto si falla un Landing point")
    print("7- Req. 6.  Conocer ancho de banda de un paus")
    print("8- Req. 7.  Ruta minima entre dos IP dadas")
    print("9- Req. 8.  Grafica de los requerimientos.")
    print("0- Salir")
    print("********************************************")

database = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        database = controller.init()
        controller.loadlpoints(database,lpoints)
        controller.loadconnections(database, connections)
        controller.loadcountries(database, countries)

    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)
