import numpy as np
from taller import Taller
import csv
class ManejadorTalleres:
    __listaTalleres:list
    __incremento:int
    __cantidad:int
    __dimension:int
    def __init__(self,dimension=2,incremento=1) -> None:
        self.__listaTalleres=np.empty(dimension,dtype=Taller)
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=incremento
    def agregarTaller(self,taller):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__listaTalleres.resize(self.__dimension)
        self.__listaTalleres[self.__cantidad]=taller
        self.__cantidad+=1
    
    def leerArchivo(self):
        file=open('Talleres.csv',encoding='utf-8')
        reader=csv.reader(file,delimiter=';')
        primerLinea=True
        for row in reader:
            if primerLinea:
                self.__dimension=int(row[0])
                self.__listaTalleres.resize(self.__dimension)
                primerLinea=False
            else:
                unTaller=Taller(int(row[0]),row[1],int(row[2]),int(row[3]))
                self.agregarTaller(unTaller)
    
    def encontrarTaller(self,id):
        i=0
        while i<len(self.__listaTalleres):
            if self.__listaTalleres[i].getID()==id:
                return self.__listaTalleres[i]
                i=len(self.__listaTalleres)
            i+=1
    
    def inscribir(self,listaInscripciones,listaPersonas):
        unTaller=self.encontrarTaller(int(input('Ingrese ID del taller para realizar la inscripción: ')))
        if unTaller.getVacantes()==0:
            print('No existen vacantes disponibles')
        else:
            unTaller.inscribirPersona(listaPersonas.crearPersona(),input('Ingrese fecha de inscripción: '),listaInscripciones)

    def consultarInscriptos(self,listaInscripciones):
        ID=input('Ingrese el identificador del taller: ')
        i=0
        while i<len(self.__listaTalleres):
            if self.__listaTalleres[i].getNombre()==ID:
                listaInscripciones.listarPersonas(self.__listaTalleres[i])
                i=len(self.__listaTalleres)
            i+=1
    def __str__(self) -> str:
        s=''
        for taller in self.__listaTalleres:
            s+=str(taller) + '\n'
        return s