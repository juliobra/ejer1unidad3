from claseFacultad import Facultad
from ManejaFacultades import ManejadoraFacultades
import csv
def opciones(op,manejador):
  if op==1:
    print("Ingrese el codigo de la Facultad")
    cod=int(input(""))
    manejador.buscarfacultad(cod)
  elif op==2:
    print("ingrese el nombre de la carrera")
    carrera=input("")
    manejador.buscarCarrera(carrera)
  elif op==3:
    print("sali")

def test():
  manejador = ManejadoraFacultades()
  manejador.cargarFacultades()
  manejador.mostrarFacultades()
  print(" MENU:")
  print("1: Mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.")
  print("2:  Mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.")
  print("3: Salir")
  op=int(input(""))
  opciones(op,manejador)

if __name__=='__main__':
 test()
 
#D. A través de un menú de opciones implementar las siguientes funcionalidades:

#1. Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.

#2.  Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.