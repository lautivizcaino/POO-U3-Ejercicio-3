class Persona:
    __nombre:str
    __direccion:str
    __dni:str
    def __init__(self,nombre,direccion,dni):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__dni=dni

    def getDni(self):
        return self.__dni
    def __str__(self):
        return 'Nombre:%s Direccion:%s DNI:%s'%(self.__nombre,self.__direccion,self.__dni)