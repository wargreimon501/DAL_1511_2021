class nodoarbol:
  def __init__(self,value,left=None,rigth=None):
    self.data=value
    self.left=left
    self.rigth=rigth
class arbolBB:
  def __init__(self):
    self.__root=None


  def insert(self,value):
    if self.__root==None:
      self.__root=nodoarbol(value)
    else:
      self.__insert_nodo__(self.__root,value)
  def __insert_nodo__(self,nodo,value):
    if nodo.data==value:
      pass
    elif value <nodo.data:
      if nodo.left==None:
        nodo.left=nodoarbol(value)
      else:
        self.__insert_nodo__(nodo.left,value)
    else:
      if nodo.rigth==None:
        nodo.rigth=nodoarbol(value)
      else:
        self.__insert_nodo__(nodo.rigth,value)
  #preorden y posorden
  def trasversal(self,formato):
    if formato =="inorden":
      self.recorrido_in(self.__root)
      print("inorden")
    elif formato== "preorden":
      self.recorrido_pre(self.__root)
      print("preorden")
    elif formato=="posorden":
      self.recorrido_pos(self.__root)
      print("pos orden")
  def recorrido_in(self,nodo): 
    if nodo!=None:
      self.recorrido_in(nodo.left)
      print(nodo.data,end="  ")
      self.recorrido_in(nodo.rigth)
  def recorrido_pre(self,nodo):
    if nodo!=None:
      print(nodo.data,end="  ")
      self.recorrido_pre(nodo.left)
      self.recorrido_pre(nodo.rigth)
  def recorrido_pos(self,nodo):
    if nodo!=None:
      self.recorrido_pos(nodo.left)
      self.recorrido_pos(nodo.rigth)
      print(nodo.data,end="  ")
  def busqueda(self,value):
    if self.__root ==None:
      print("arbol vacio")
      return None
    else:
      return self.busca_nodo(self.__root,value)
  def busca_nodo(self,nodo,value):
    if nodo==None: 
      print("no existe")
      return None
    elif nodo.data==value:
      print("encontrado",nodo.data)
      return nodo
    elif value <nodo.data:
      #print("buscar de lado izquierdo")
      return self.busca_nodo(nodo.left,value)
    else:
      #print("buscar de lado derecho")
      return self.busca_nodo(nodo.rigth,value)
  def remove(self,value):
      #Noexista un arbol
    if self.__root==None:
      print("Nada que eliminar")
    else:
      self.__remove(None,None,self.__root,value)
  def __remove(self,padre_hi,padre_hd,actual , value):
      if actual == None:
          print("No contiene este arbol el valor que deseas remover ")
          return None
      elif actual.data==value:
          print("Encontrado", actual.data)
          #caso 1:hoja
          if actual.left==None and actual.rigth==None:
              if padre_hi != None:
                  padre_hi=None
              else:
                  padre_hd.rigth=None
          #caso2:con un hijo
          if (actual.left != None and actual.rigth == None) or (actual.left == None and actual.rigth != None):
              print("es un nodo con un hijo ",actual.data)
              if actual.left != None:
                  actual.data = actual.left.data
                  actual.left=None
              else:
                  actual.data = actual.rigth.data
                  actual.rigth=None
          #caso3:con los dos hijos
      elif value < actual.data:
          print("Buscas a la izquierda ")
          self.__remove(actual ,None,actual.left,value)
      elif value > actual.data:
          print("buscar a la derecha")
          self.__remove(None ,actual,actual.rigth,value)
abb=arbolBB()
abb.insert(55)
abb.insert(14)
abb.insert(27)
abb.insert(15)
abb.insert(21)
abb.insert(80)
abb.insert(27)
abb.insert(6)
abb.insert(3)
abb.insert(8)
abb.trasversal("inorden")
abb.trasversal("preorden")
abb.trasversal("posorden")
print("++++++++++++++++++++++++++++")
abb.busqueda(3)
abb.remove(8)
print("++++++++++++++++++++++++++++")
abb.trasversal("inorden")
abb.trasversal("preorden")
abb.trasversal("posorden")