"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
#__________________________________________________________________________
# Inicialización del Catálogo del grafo
def init():
    database = model.newdatabase()
    return database 

#__________________________________________________________________________
# Funciones para la carga de datos
def loadlpoints(database, lpoints):
    lpoints = cf.data_dir + lpoints
    input_file = csv.DictReader(open(lpoints, encoding="utf-8"),
                                delimiter=",")
    for vertex in input_file:
        model.loadlpoints(database, vertex)
    return database

def loadconnections(database, connections):
    connections = cf.data_dir + connections
    input_file = csv.DictReader(open(connections, encoding="utf-8-sig"),
                                delimiter=",")
    for connection in input_file:
        model.loadconnections(database, connection)
    return database

def loadcountries(database, countries):
    countries = cf.data_dir + countries 
    input_file = csv.DictReader(open(countries, encoding="utf-8"),
                                delimiter=",")
    for countrie in input_file:
        model.loadcountries(database, countrie)
    return database

#__________________________________________________________________________
# Funciones de ordenamiento

#__________________________________________________________________________
# Funciones de consulta sobre el catálogo
