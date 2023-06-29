'''Dise˜ne una funci´on que calcule la cantidad de carne de aves en kilos
si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6
kilos, 7 kilos y 1 kilo respectivamente.
'''

def cantidadCarneDeAves():
    numGallinas = int(input('Ingrese la cantidad de gallinas: '))
    pesoGallinas = 6*numGallinas

    numGallos = int(input('Ingrese la cantidad de gallos: '))
    pesoGallo = 7*numGallos

    numPollitos = int(input('Ingrese la cantidad de pollitos: '))
    pesoPollitos = 1*numPollitos

    total=('La cantidad de aves en kilos es de: '+str(pesoGallinas+pesoGallo+pesoPollitos))

    return total

resultado = cantidadCarneDeAves()
print(resultado)