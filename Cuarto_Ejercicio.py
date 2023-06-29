'''Dise˜ne un programa que muestre las tablas de multiplicar del 1 al 9.'''

for num_tabla in range (1,10):
    print("\n")
    for tablas in range (1,11,1):
        result = tablas*num_tabla
        print(num_tabla, 'X', tablas, '=', result)