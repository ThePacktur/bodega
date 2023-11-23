from Producto import Producto
from DAO import DAO 


def registrar():
    print("******Registro de Productos*****")
    codigo = input("Ingrese el codigo del Producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantiad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    color = input("Ingrese el color del pruducto: ")
    origen = input("ingrese el origen del producto: ")
    tamanio = int(input("Ingrese el valor del tamanio: "))
    tipo = input("ingrese el tipo de producto: ")
    pro = Producto(nombre,cantidad,precio,color,origen,codigo,tamanio,tipo)
    d = DAO()
    d.registrar(pro)

def eliminar():
    cod = buscarCodigo()
    if cod!=None:
        d = DAO()
        d.eliminar(cod.get_codigo())
    else:
        print("El codigo no existe!!")


def buscarCodigo() ->Producto:
    codigo = input("Ingrese el codigo del producto: ")
    d = DAO()
    cod = d.buscarCodigo(codigo,)
    if cod!=None:
        print(cod)
    else:
        print("no se encontro el codigo!!!")
    return cod


def mostrarTodo():
    d = DAO()
    list = d.mostrarTodo()
    for producto in list:
        print("------------")
        print(producto)
        print("------------")


def modificar():
    cod = buscarCodigo()
    if cod!=None:
        d = DAO()
        cod.set_codigo(preguntarCambio("Codigo: ",cod.get_codigo()))
        cod.set_nombre(preguntarCambio("Nombre: ",cod.get_nombre()))
        cod.set_precio(preguntarCambio("Precio: ",cod.get_precio()))
        cod.set_color(preguntarCambio("Color: ",cod.get_color()))
        cod.set_origen(preguntarCambio("Origen: ",cod.get_origen()))
        cod.set_tamanio(preguntarCambio("Tamanio: ",cod.get_tamanio()))
        cod.set_tipo(preguntarCambio("Tipo: ",cod.get_tipo()))
        d.modificar(cod)
    else:
        print("El codigo no existe!!!")

def preguntarCambio(valor:str,atributo):
    opcion = input(f"Desea modificar el {valor}:s/n")
    if opcion.lower()=="s":
        values = input(f"Ingrese el {valor}: ")
        return values
    else:
        return atributo

def mostrarOrigenTipo() ->Producto:
    pass

def buscarOrigenCantidadMayor():
    pass

def menu():
    print("Bienvenido")
    print("----opciones-----")
    print("1.- Registrar Producto ")
    print("2.- Eliminar Producto ")
    print("3.- Buscar Producto por Codigo ")
    print("4.- Mostrar Todo")
    print("5.- Modificar")
    #print("6.- Mostrar por origen y tipo")
    #print("7.-buscar por Origen y cantidad que sea mayor ")
    print("8.- Salir ")
    opcion = input("Ingrese una opcion: ")
    if opcion =="1":
        registrar()
    elif opcion == "2":
        eliminar()
    elif opcion == "3":
        buscarCodigo()
    elif opcion == "4":
        mostrarTodo()
    elif opcion == "5":
        modificar()
    #elif opcion == "6":
    #    mostrarOrigenTipo()
    #elif opcion == "7":
    #    buscarOrigenCantidadMayor()
    elif opcion =="8":
        print("Gracias por ultilizar el programa, vuelva pronto.")
        return True
    else:
        print("La opcion ingresada no es valida, intentelo nuevamente.")


while menu() !=True:
    pass

