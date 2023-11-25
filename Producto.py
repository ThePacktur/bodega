class Producto:
    def __init__(self,nombre:str,cantidad:int,precio:float,color:str,origen:str,codigo:str,tamanio:int,tipo:str,idProducto: int =0):
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio
        self.__color = color
        self.__origen = origen
        self.__codigo = codigo
        self.__tamanio = tamanio
        self.__tipo = tipo
        self.__idProducto = idProducto
        
    def get_nombre(self):
        return self.__nombre
    
    def get_cantidad(self):
        return self.__cantidad
    
    def get_precio(self):
        return self.__precio
    
    def get_color(self):
        return self.__color
    
    def get_origen(self):
        return self.__origen
    
    def get_codigo(self):
        return self.__codigo
    
    def get_tamanio(self):
        return self.__tamanio
    
    def get_tipo(self):
        return self.__tipo
    
    def get_idProducto(self):
        return self.__idProducto
    

    def set_nombre(self,nombre):
        self.__nombre = nombre 

    def set_cantidad(self,cantidad):
        self.__cantidad = cantidad
    
    def set_precio(self,precio):
        self.__precio = precio

    def set_color(self,color):
        self.__color = color

    def set_origen(self,origen):
        self.__origen = origen
    
    def set_codigo(self,codigo):
        self.__codigo = codigo

    def set_tamanio(self,tamanio):
        self.__tamanio = tamanio

    def set_tipo(self,tipo):
        self.__tipo = tipo

    def set_idProducto(self,idProducto):
        self.__idProducto = idProducto

    def __str__(self):
    
        txt = f"\nNombre: {self.__nombre}"
        txt += f"\ncantidad: {self.__cantidad}"
        txt += f"\nprecio: {self.__precio}"
        txt += f"\ncolor: {self.__color}"
        txt += f"\nOrigen: {self.__origen}"
        txt += f"\nCodigo: {self.__codigo}"
        txt += f"\nTamanio: {self.__tamanio}"
        txt += f"\nTipo: {self.__tipo}"
        
        return txt