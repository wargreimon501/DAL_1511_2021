class Nodo :
    def __init__(self,value,siguiente= None):
        self.data= value   # falta encapsulamiento
        self.siguiente=siguiente
    def trasversal(self):
        print(f"{self.data}")
        print("")
class LinKedList:
    def __init__(self):
        self.__head=None
    def is_empty(self):
        return self.__head==None
    def append (self,value):
        nuevo= Nodo (value)
        if self.__head == None: # NOTE: self.is_empty()
            self.__head=nuevo
        else:
            curr_node=self.__head
            while curr_node.siguiente !=None:
                curr_node=curr_node.siguiente
            curr_node.siguiente=nuevo
    def trasversal(self):
        curr_node = self.__head
        while curr_node !=None:
            print(f"{curr_node.data }->", end="")
            curr_node=curr_node.siguiente
        print("")
    def tail (self):
        curr_node = self.__head
        while curr_node.siguiente !=None:
            curr_node=curr_node.siguiente
        return curr_node
    def remove (self,value):
        curr_node=self.__head
        if self.__head.data == value:
            self.__head=self.__head.siguiente
        else:
            anterior= None
            while curr_node.data != value and curr_node.siguiente !=None:
                anterior=curr_node
                curr_node=curr_node.siguiente
            if curr_node.data==value:
                anterior.siguiente=curr_node.siguiente
            else:
                print("El dato no existe en la lista")
    def preppend(self , value):
        nuevo=Nodo(value,self.__head)
        self.__head = nuevo
    def get (self,posicion = None):#por defecto regresa el ultimo

        dato = None
        if posicion== None:
            dato = self.tail().data
        else:
            curr_node=self.__head
            while curr_node.data == posicion:
                contador=0
                contador=contador + 1
                dato=contador

            return dato
    def add_before(self,reference_value,value):
        nuevo= Nodo(value)
        curr_node=self.__head
        while curr_node.data != reference_value and curr_node.siguiente != None:#busca nuestro nodo de referencia.
            curr_new=curr_node
            curr_node= curr_node.siguiente
        if curr_node.data == reference_value and curr_node.data != self.__head.data:#nodo igual a referencia y diferente a head.
            curr_new.siguiente=nuevo
            curr_new.siguiente.siguiente=curr_node
        else:#si no es el caso entra aqui y pregunta nodo igual a head.
            if curr_node.data == reference_value:
                self.__head=nuevo
                nuevo.siguiente=curr_node
    def busqueda(self,value):
     curr_node=self.__head
     if self.__head.data == value:
         return self.__head.data
     else:
         anterior= None
         while curr_node.data != value and curr_node.siguiente !=None:
             anterior=curr_node
             curr_node=curr_node.siguiente
             return curr_node.siguiente.siguiente.siguiente.siguiente.data
         if curr_node.data==value:
             anterior.siguiente=curr_node.siguiente
             
         else:
             print("El dato no existe en la lista")
             