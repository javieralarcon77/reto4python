def menuProductos():
    opc = 6    
    while opc > 6:
        print('')
        print('Agregar Productos')
        print('1: Ingresar')
        print('2: Listar')
        print('3: Consultar')
        print('4: Actualizar')
        print('5: Eliminar')
        print('6: Regresar')
        opc = int(input('Ingrese una opcion: '))
    return opc

def mainProductos(productos:list):
    opc = menuProductos()
    while opc < 6:
        print('datos de productos')
        if opc == 1: #ingresar
            productos.append( input('Ingrese el nombre del nuevo productos: ') )

        if opc == 2: #listar
            print(productos)

        if opc == 3: #consultar
            search = input('Ingrese el nombre del producto a buscar')
            msg = 'No esta el producto'
            for producto in productos:
                if( producto == search ):
                    msg = 'El producto si existe'
            
            print( msg )
                
        opc = menuProductos()
    
