import os
menu = [ 'leer' , 'crear' , 'modificar' , 'eliminar' ]
campos_save = ["ID" , "Nombre del cliente" , "Dirección cliente" , "Cantidad de productos" , "Employee" ]
power = True
print('Bienvenido a FacturaSoft')

while power:
    c = 1
    for i in menu:
        print( str(c) + ' -- ' + i + ' factura' )
        c+=1
    entrada = input()
    entrada = int(entrada)
    if entrada == 2:
        data_create = []
        os.system("cls")
        for i in campos_save:
           temp = input(i + ' \n')
           data_create.append(temp)
        print(data_create)




