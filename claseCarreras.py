class CarrerasFac:
  __codigo=int
  __direccion= str
  __nombre=str
  __fechaInicio=str
  __duracion= int
  __titulo=str
  def __init__(self,codigo,direccion, nombre, fechaInicio, duracion, titulo):
    self.__codigo=codigo
    self.__direccion= direccion
    self.__nombre= nombre
    self.__fechaInicio= fechaInicio
    self.__duracion= duracion
    self.__titulo= titulo


  def getcodigo(self):
        return self.__codigo

  def getdireccion(self):
        return self.__direccion

  def getnombre(self):
        return self.__nombre

  def getfechaInicio(self):
        return self.__fechaInicio

  def getDuracion(self):
        return self.__duracion

  def getTitulo(self):
        return self.__titulo

  def __str__(self):
        return f"Carrera: {self.getcodigo()}, {self.getdireccion()}, {self.getnombre()}, {self.getfechaInicio()}, {self.getDuracion()}, {self.getTitulo()}"

 

    
  

 
    