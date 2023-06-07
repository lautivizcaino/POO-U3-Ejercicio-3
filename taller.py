from inscripcion import Inscripcion
from persona import Persona
from manejaInscripciones import ManejadorInscripciones
class Taller:
    __idTaller:int
    __nombre:str
    __vacantes:int
    __montoInscripcion:int
    __inscripciones:list
    def __init__(self,idTaller,nombre,vacantes,monto):
        self.__idTaller=idTaller
        self.__nombre=nombre
        self.__vacantes=vacantes
        self.__montoInscripcion=monto
        self.__inscripciones=[]
    
    def getID(self):
        return self.__idTaller
    def getVacantes(self):
        return self.__vacantes
    def getNombre(self):
        return self.__nombre
    def getMonto(self):
        return self.__montoInscripcion
    
    def getInscripciones(self):
        return self.__inscripciones
    
    def inscribirPersona(self,persona,fecha,listaInscripciones,pago=False):
        unaInscripcion=Inscripcion(fecha,pago,self,persona)
        listaInscripciones.agregarInscripcion(unaInscripcion)
        self.__inscripciones.append(unaInscripcion)
        self.__vacantes-=1

    def mostrarInscripciones(self):
        for inscripcion in self.__inscripciones:
            print(inscripcion)

    def __str__(self):
        return 'ID:%s Nombre:%s Vacantes:%s Monto:%s'%(self.__idTaller,self.__nombre,self.__vacantes,self.__montoInscripcion)
