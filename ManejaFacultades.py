from claseFacultad import Facultad
from claseCarreras import CarrerasFac 
import csv
class ManejadoraFacultades:
    def __init__(self):
        self.__facultades = []
        self.__carreras=[]
   
    def cargarFacultades(self):
        with open('facultades.csv', 'r', encoding='latin-1') as file: 
     
            lineas = file.readlines()
#La línea lineas = file.readlines() lee todas las líneas del archivo abierto file y las guarda en una lista llamada lineas. Cada elemento de la lista representa una línea del archivo.

#El método readlines() es utilizado en archivos de texto para leer todas las líneas y devolverlas como una lista de cadenas de texto. Cada cadena de texto en la lista corresponde a una línea completa del archivo, incluyendo los caracteres de nueva línea al final de cada línea.
            i = 0
            while i < len(lineas):
                datos_facultad = lineas[i].strip().split(",")   
 #se obtiene una línea del archivo facultades.csv utilizando lineas[i]. Esta línea se limpia de caracteres de espacio en blanco al principio y al final utilizando strip(). Luego, se divide en una lista de valores separados por comas utilizando split(",").
                codigo = int(datos_facultad[0])
                nombre = datos_facultad[1]
                direccion = datos_facultad[2]
                localidad = datos_facultad[3]
                telefono = datos_facultad[4]
                facultad = Facultad(codigo, nombre, direccion, localidad, telefono)

                i += 1
                while i < len(lineas) and lineas[i].strip().startswith(str(codigo)):
#i < len(lineas): Esta parte de la condición verifica si el índice i es menor que la longitud de la lista lineas. El bucle continuará mientras i sea menor que la cantidad de elementos en lineas, evitando un desbordamiento de índice.

#lineas[i].strip().startswith(str(codigo)): Esta parte verifica si la línea actual, después de eliminar los espacios en blanco iniciales y finales con .strip(), comienza con un número convertido a cadena str(codigo). La función .startswith() verifica si una cadena comienza con la subcadena proporcionada.
                    datos_carrera = lineas[i].strip().split(",")
                    codigo = int(datos_carrera[0])
                    direccion = datos_carrera[1]
                    nombre = datos_carrera[2]
                    fechaInicio= datos_carrera[3]
                    duracion= datos_carrera[4]
                    titulo = datos_carrera[5]
                    carreras = CarrerasFac(codigo, direccion, nombre,fechaInicio,duracion, titulo)
                    self.__carreras.append(carreras)
                    i += 1
               
                self.__facultades.append(facultad)

    def mostrarFacultades(self):
        for facultad in self.__facultades:
            print(facultad)
    def buscarfacultad(self,codigo):
        i=0  
        while i< len(self.__facultades):
                  if codigo == self.__facultades[i].getCodigo():
                    print("Nombre facultad: {}".format(self.__facultades[i].getnombre()))
                    for facultad in self.__facultades:
                      
                       for carrera in self.__carreras:
                         print("Carrera: {}, duracion {}, codico carrera {}".format(carrera.getnombre(),carrera.getDuracion(),carrera.getcodigo()))
                         i += 1
                         return -1
                    
    def buscarCarrera(self,nombre):
          #2.  Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.
      i=0
      while i< len(self.__facultades):
        for facultad in self.__facultades:
          for carrera in self.__carreras:
            if nombre== carrera.getnombre():
                 print("codigo carrera: {},codigo fc: {}, nombre fac: {}, localidad: {}".format(self.__carreras.getcodigo(),self.__facultad.getCodigo(),self.__facultad.getNombre(),self.__facultades.getlocalidad()))
      i+=1
                   
                   

                  