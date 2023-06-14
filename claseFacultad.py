from claseCarreras import CarrerasFac
class Facultad:
  __cod: int
  __nom: str
  __dir: str
  __loc: str
  __tel: str
  __carreras: list
 
 
  def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carreras = []
  
  
  def getCodigo(self):
    return self.__codigo
  def getnombre(self):
    return self.__nombre
  
  def getlocalidad(self):
    return self.__localidad

  

  def __str__(self):
      carrera_str = "\n".join(str(carrera) for carrera in self.__carreras)
      return f"Facultad: {self.__codigo}, {self.__nombre}, {self.__direccion}, {self.__localidad}, {self.__telefono}\n{carrera_str}"
  
 #'''' def __str__ (self):
  #  cadena='facultad:\n'
   # cadena+='codigo ,nombre , direccion, localiad, telefono: {} {} {} {} {} \n'.format(self.__codigo,self.__nombre,self.__direccion,self.__localidad,self.__telefono)
 #   return cadena'''
    
    
  
  