'''Desarrollar un programa que imprima el cuadrado del n´umero que el
usuario ingresa mientras que el n´umero ingresado no sea negativo'''

while True:
    userNum = int(input('Ingrese un número: '))
    if userNum < 0:
        print('El número es negativo')
        break
    else:
        oper=userNum*userNum
        print('El número al cuadrado es: ',str(oper))