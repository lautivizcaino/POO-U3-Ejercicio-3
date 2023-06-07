from manejaTalleres import ManejadorTalleres
from manejaPersonas import ManejadorPersonas
from manejaInscripciones import ManejadorInscripciones

class Menu:
    __opcion:int
    def __init__(self):
        self.__opcion=6
    def opciones(self,listaTalleres,listaPersonas,listaInscripciones):
        while self.__opcion!=0:
            print('\n1 - Inscribir una persona en un taller\n2 - Consultar inscripción\n3 - Consultar inscriptos\n4 - Registrar pago\n5 - Guardar Inscripciones\n')
            self.__opcion=int(input('Ingrese la opción a ejecutar: '))
            if self.__opcion==1:
                print('\nOPCION 1')
                listaTalleres.inscribir(listaInscripciones,listaPersonas)

            elif self.__opcion==2:
                print('\nOPCIÓN 2')
                listaInscripciones.consultarInscripcion()

            elif self.__opcion==3:
                print('\nOPCIÓN 3')
                listaTalleres.consultarInscriptos(listaInscripciones)

            elif self.__opcion==4:
                print('\nOPCIÓN 4')
                listaInscripciones.registrarPago()

            elif self.__opcion==5:
                print('\nOPCIÓN 5')
                listaInscripciones.generarArchivo()

        else:
            print('\nHa salido del sistema.')