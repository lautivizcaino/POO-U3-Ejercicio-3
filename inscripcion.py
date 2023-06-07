from persona import Persona
class Inscripcion:
    __fecha:str
    __pago:bool
    __taller:object
    __persona:object
    def __init__(self,fecha,pago,taller,persona):
        self.__fecha=fecha
        self.__pago=pago
        self.__taller=taller
        self.__persona=persona
    
    def getFecha(self):
        return self.__fecha
    def getPago(self):
        return self.__pago
    def getIdTaller(self):
        return self.__taller.getID()
    def getDniPersona(self):
        return self.__persona.getDni()

    def getDNI(self):
        return self.__persona.getDni()
    def getNomTaller(self):
        return self.__taller.getNombre()
    def getMontoTaller(self):
        return self.__taller.getMonto()
    def getPersona(self):
        return self.__persona
    def setPago(self,estado):
        self.__pago=estado
    def __str__(self) -> str:
        cadena='\nFecha de inscripción: %s Pago: %s '%(self.__fecha,self.__pago)
        cadena+=str(self.__persona)
        return cadena
