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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from haversine import haversine as hs
assert cf
from DISClib.ADT.graph import gr

#TODO revisar si se puede eliminar la informacion en el mapLP
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newdatabase():
    database = {'maplpoints':None,
                'maplpcountries':None,
                'mapcountinents':None,
                'mapconnections':None,
                'ltvertex': None,
                'graph':None}

    database['maplpoints'] = createmap(3400)
    database['maplpcountries'] =createmap(600) 
    database['mapcountinents'] = createmap(20)
    database['mapconnections'] = createmap(3000)
    database['ltvertex'] = lt.newList('ARRAY_LIST')
    database['graph'] = gr.newGraph(datastructure='ADJ_LIST',
                                directed=True,
                                size=1700,
                                comparefunction=None)
    return database
#_______________________________________________________________
# Funciones para agregar informacion al catalogo
def loadlpoints(database, vertex):
    ltvertex = database['ltvertex']
    graph = database['graph']
    maplpoints = database['maplpoints']
    lp = vertex['landing_point_id']
    maplpcountries = database['maplpcountries']

    lt.addLast(ltvertex, vertex)
    addvertexgraph(graph, lp)
    addvertexmaplp(maplpoints, lp, vertex)
    addvertexmapct(maplpcountries, lp, vertex)
    return database

def loadconnections(database, connection):
    mapconnections = database['mapconnections']+
    destination = connection['destination']
    origin = connection['origin']
    cablename = connection['cable_name']
    relation = (origin, cablename)

    completemap(mapconnections, destination, relation) 
    #esta funcion identifica cuantos cables llegaran a un vertice 

def loadcountries(database, countries):
    pass

def createvertex(database):
    mapconnections = database['mapconnections']
    pass






#_______________________________________________________________
# Funciones para creacion de datos
def addvertexgraph(graph, lp):
    # agrega los vertices al grafo
    if not gr.containsVertex(graph, lp):
        gr.insertVertex(graph, lp)
    return graph

def addvertexmaplp(maplpoints, lp, vertex):
    #guarda todo los vertices en un map
    entry = mp.get(maplpoints, lp)
    if entry is None:
        mp.put(maplpoints, lp, vertex)
    return maplpoints

def addvertexmapct(maplpcountries, lp, vertex):
    #cladifica los vertices por paises
    countrie = vertex['name']
    countrie = countrie.replace(' ','').lower().replace(',',' ')
    countrie = countrie.split()
    if len(countrie) == 1:
        completemap(maplpcountries, countrie[0], lp)
    else:
        completemap(maplpcountries, countrie[1], lp)


def completemap(map, key, value):
    entry = mp.get(map,key)
    if entry is None:
        datentry = completelist('ARRAY_LIST', value)
        mp.put(map,key,datentry)
    else:
        datentry = me.getValue(entry)
        lt.addLast(datentry, value)
    return map

def completelist(type, data):
    list = lt.newList(type)
    lt.addLast(list, data)
    return list

def createmap(size): 
    map = mp.newMap(size,
                maptype='PROBING',
                loadfactor=0.5,
                comparefunction=None)
    return map
    
#_______________________________________________________________
# Funciones de consulta

#_______________________________________________________________
# Funciones utilizadas para comparar elementos dentro de una lista

#_______________________________________________________________
# Funciones de ordenamiento
