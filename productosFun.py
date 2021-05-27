def menuProductos():
    opc = 7    
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


            

        if opc == 4: #actualizar
            search = input('Ingrese el nombre del producto a buscar')

            encontro = False
            for i in range( len( productos ) ):
                if( productos[i] == search ):
                    new = input("Ingrese el nuevo nombre")
                    productos[i] = new
                    print('Producto actualizado con exito')
                    print('')
                    encontro = True

            if encontro == False:
                print( "El producto ingresado no existe" )
        

        opc = menuProductos()
    
