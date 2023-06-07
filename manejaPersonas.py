from persona import Persona
class ManejadorPersonas:
    __listaPersonas:list
    def __init__(self):
        self.__listaPersonas=[]
    def agregarPersona(self,persona):
        self.__listaPersonas.append(persona)
    def crearPersona(self):
        unaPersona=Persona(input('Ingrese nombre de la persona: '),input('Ingrese direccion: '),input('Ingrese dni: '))
        self.agregarPersona(unaPersona)
        return unaPersona
    def __str__(self):
        s=''
        for persona in self.__listaPersonas:
            s+=str(persona) + '\n'
        return s