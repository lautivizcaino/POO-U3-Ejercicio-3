from manejaTalleres import ManejadorTalleres
from manejaPersonas import ManejadorPersonas
from manejaInscripciones import ManejadorInscripciones
from menu import Menu
def test():
    listaTalleres=ManejadorTalleres()
    listaTalleres.leerArchivo()
    listaPersonas=ManejadorPersonas()
    listaInscripciones=ManejadorInscripciones()
    menu=Menu()
    menu.opciones(listaTalleres,listaPersonas,listaInscripciones)

if __name__ =='__main__':
    test()