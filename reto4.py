from productosFun import mainProductos

productos = []

def menuPrincipal():
    #se inicializa la opcion de manera que la validacion del while de true
    opc = 6    
    while opc > 5:
        print('')
        print('Menu Principal')
        print('1: Agregar Producto')
        print('2: Agregar Empleado')
        print('3: Agregar Cliente')
        print('4: Registrar Venta')
        print('5: Salir')
        opc = int(input('Ingrese una opcion: '))

    return opc

#inicio de ejercicio
opc = menuPrincipal()

while opc != 6:
    if opc == 1:
        mainProductos(productos)
    
    opc = menuPrincipal()

