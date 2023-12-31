from Producto import Producto
import credencial
import mysql.connector

class DAO:
    def __init__(self):
        pass

    def __conectar(self):
        self.__conexion = mysql.connector.connect(**credencial.get_credenciales())
        self.__cursor = self.__conexion.cursor()

    def __cerrar(self):
        self.__conexion.commit()
        self.__conexion.close()

    def registrar(self,pro:Producto):
        self.__conectar()
        sql = "INSERT INTO producto (nombre,cantidad,precio,color,origen,codigo,tamanio,tipo) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (pro.get_nombre(),pro.get_cantidad(),pro.get_precio(),pro.get_color(),pro.get_origen(),pro.get_codigo(),pro.get_tamanio(),pro.get_tipo())
        self.__cursor.execute(sql,values)
        self.__cerrar()

    

    def eliminar(self, codigo:str):
        self.__conectar()
        sql = "DELETE FROM producto WHERE codigo = %s "
        values = (codigo,)
        self.__cursor.execute(sql,values)
        self.__cerrar()

    def buscarCodigo(self, codigo:str):
        self.__conectar()
        sql = "SELECT * FROM producto WHERE codigo = %s"
        values = (codigo,)
        self.__cursor.execute(sql,values)
        buscar = self.__cursor.fetchone()
        self.__cerrar()
        if buscar != None:
            pro = Producto(buscar[1],buscar[2],buscar[3],buscar[4],buscar[5],buscar[6],buscar[7],buscar[8],buscar[0],)
            return pro
        else: 
            return None
        
    def mostrarTodo(self):
        self.__conectar()
        sql = "SELECT * FROM producto"
        self.__cursor.execute(sql)
        respuesta = self.__cursor.fetchall()
        productos = []
        for tuplas in respuesta:
            cod = Producto(tuplas[1],tuplas[2],tuplas[3],tuplas[4],tuplas[5],tuplas[6],tuplas[7],tuplas[8],tuplas[0],)
            productos.append(cod)
        self.__cerrar()
        return productos
    
    def modificar(self,pro:Producto):
        self.__conectar()
        sql = "UPDATE producto SET nombre = %s,cantidad = %s,precio =%s,color =%s,origen =%s,codigo = %s,tamanio =%s,tipo =%s WHERE idProducto =%s"
        values = (pro.get_nombre(),pro.get_cantidad(),pro.get_precio(),pro.get_color(),pro.get_origen(),pro.get_codigo(),pro.get_tamanio(),pro.get_tipo(),pro.get_idProducto())
        self.__cursor.execute(sql,values)
        self.__cerrar

    def mostrarOrigenTipo(self,origen:str,tipo:str):
        self.__conectar()
        sql = "SELECT * FROM producto WHERE origen = %s AND tipo =%s"
        values = (origen,tipo)
        self.__cursor.execute(sql,values)
        tuplass  = self.__cursor.fetchall()
        self.__cerrar() 
        contador = 1
        for pro in tuplass:
            #print(pro)
            cod = Producto(pro[1],pro[2],pro[3],pro[4],pro[5],pro[6],pro[7],pro[8],pro[0])
            print(f'{"-"*9} producto {+contador} {"-"*9}\n\
{cod}\n\
{"-"*20}')

    def buscarOrigenCantidadMayor(self,genero:str,cantidad:int):
        self.__conectar()
        sql = "SELECT * FROM producto WHERE origen =%s AND cantidad > %s"
        values = (genero,cantidad)
        self.__cursor.execute(sql,values)
        product = self.__cursor.fetchall()
        self.__cerrar()
        for pro in product:
           cod = Producto(pro[1],pro[2],pro[3],pro[4],pro[5],pro[6],pro[7],pro[8],pro[0])
           print(cod)

    def odenarSumarTipoCantidad(self,tipo:str):
        self.__conectar()
        sql = "SELECT tipo, SUM(cantidad) AS total FROM producto WHERE tipo =%s  GROUP BY tipo HAVING SUM(cantidad);"
        values = (tipo,)
        
        self.__cursor.execute(sql,values)
        resultado = self.__cursor.fetchall()
        self.__cerrar()
        return resultado