from os import remove

opcion = 1 
productos = []

print()
while opcion != 0:
    print()
    print()
    print("*********** LISTA DE SUPERMERCADO ***********")
    print()
    print("Opcion 1 = Ingresar una producto")
    print("Opcion 2 = Mostrar todos los productos")
    print("Opcion 3 = Buscar un producto por codigo")
    print("Opcion 4 = Editar un producto por codigo")
    print("Opcion 5 = Eliminar un codigo")
    print("Opcion O = Salir ")
    print()
    opcion = int(input("SELECCIONE UNA OPCIÓN = "))
    print()
    if(opcion == 1):
        producto = {}
        print("----------INGRESAR PRODUCTO-----------")
        producto['codigo'] = int(input("Digite el codigo del producto = "))
        producto['nombre'] = input("Digite el nombre del producto = ")
        producto['precio'] = int(input("Digite el precio del producto = "))
        productos.append(producto)
        print()
        print("Producto registrado con exito")
        print()
    elif(opcion == 2):
        if(len(productos) > 0):
            print("----------LISTADO DE PRODUCTOS-----------")
            print(f"listado de productos registrados => {productos}")
        else:
            print("la lista no tiene elementos!")
    elif(opcion == 3):
        print()
        print("----------BUSCAR PRODUCTO-----------")
        buscado = int(input("Ingrese el codigo del producto a buscar = "))
        for producto in productos:
            if(buscado == producto['codigo']):
                print(f"Producto encontrado => {producto}")
                print()
            else:
                print("Producto no encontrado =/ ")
    elif(opcion == 4):
        print("----------EDITAR PRODUCTO-----------")
        print()
        buscado = int(input("Ingrese el codigo del producto a editar = "))
        for producto in productos:
            if(buscado == producto['codigo']):
                print (f"producto a editar {buscado}")
                producto['codigo'] = int(input("Ingrese el  NUEVO codigo del producto = "))
                producto['nombre'] = (input("Ingrese el  NUEVO nombre del producto = "))
                producto['precio'] = int(input("Ingrese el  NUEVO precio del producto = "))
                print("Codigo editado con exito!")
            else:
                print("Producto no encontrado =/ ")
    elif(opcion == 5):
        print("----------ELIMINAR PRODUCTO-----------")
        print()
        buscado = int(input("Ingrese el codigo del producto a eliminar = "))
        for producto in productos:
            if(buscado == producto['codigo']):

                print(f"Producto eliminar => {producto}")
                productos.remove(producto)
                print("Producto eliminado con exito! ")
                break
            else:
                print("Producto no encontrado =/ ")
    else:
        print("Opcion invalida")
        print()