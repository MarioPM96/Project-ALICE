menu = [ 'leer' , 'crear' , 'modificar' , 'eliminar' ]

power = True

print('Bienvenido a FacturaSoft')

while power:
    c = 1
    for i in menu:
        print( str(c) + ' -- ' + i + ' factura' )
        c+=1
    input()
