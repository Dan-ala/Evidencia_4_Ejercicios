'''Mi mamá me manda a comprar P panes a $ 300 cada uno, M bolsas
de leche a $ 3300 cada una y H huevos a $ 350 cada uno. Hacer un
programa que me diga las vueltas (o lo que quedo debiendo) cuando
me da un billete de B pesos.
'''

def compra():
    p=int(input('¿Cuántos panes va a comprar?: '))
    operP = p*300
    m=int(input('¿Cuántas bolsas de leche va a comprar?: '))
    operM = m*3300
    h=int(input('¿Cuántos huevos va a comprar?: '))
    operH = h*350

    totalDeLaCompra=operP+operM+operH

    print('La compra tiene un total de: ',str(totalDeLaCompra))
    return totalDeLaCompra



def calculo(totalDeLaCompra):
    billeteInicial=int(input('¿Con cuánto va a pagar?: '))

    if totalDeLaCompra>billeteInicial:
        print('Queda debiendo: ',str(totalDeLaCompra-billeteInicial))
    elif totalDeLaCompra==billeteInicial:
        print('No tiene cambio')

    else:
        print('Le sobran: ',str(billeteInicial-totalDeLaCompra))

totalDeLaCompra = compra()
calculo(totalDeLaCompra)