from inscripcion import Inscripcion
import numpy as np
import csv
class ManejadorInscripciones:
    __listaInscripciones:list
    __dimension:int
    __cantidad:int
    __incremento:int
    def __init__(self,dimension=1,incremento=1):
        self.__listaInscripciones=np.empty(dimension,dtype=Inscripcion)
        self.__dimension=dimension
        self.__cantidad=0
        self.__incremento=incremento
    
    def agregarInscripcion(self,inscripcion):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__listaInscripciones.resize(self.__dimension)
        self.__listaInscripciones[self.__cantidad]=inscripcion
        self.__cantidad+=1
    
    def consultarInscripcion(self):
        dni=input('Ingrese DNI de la persona: ')
        for inscripcion in self.__listaInscripciones:
            if inscripcion.getDNI()==dni:
                print('Nombre:%s Monto:%.2f'%(inscripcion.getNomTaller(),inscripcion.getMontoTaller()))

    def listarPersonas(self,taller):
        for inscripcion in taller.getInscripciones():
            print(inscripcion.getPersona())
    
    def registrarPago(self):
        dni=input('Ingrese DNI de la persona: ')
        for inscripcion in self.__listaInscripciones:
            if inscripcion.getDNI()==dni:
                inscripcion.setPago(True)

    def generarArchivo(self):
        file=open('Inscripciones.csv','w',encoding='utf-8',newline='')
        writer=csv.writer(file,delimiter=';')
        for i in range(len(self.__listaInscripciones)):
            row=[str(self.__listaInscripciones[i].getDniPersona()),str(self.__listaInscripciones[i].getIdTaller()),str(self.__listaInscripciones[i].getFecha()),str(self.__listaInscripciones[i].getPago())]
            writer.writerow(row)
        file.close()
        print('\nArchivo actualizado')
    def __str__(self):
        s=''
        for inscripcion in self.__listaInscripciones:
            s+=str(inscripcion) + '\n'
        return s