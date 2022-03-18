# Adivina adivinador....
import random
numero_aleatorio = random.randrange(5)
gane = False
print('Tenes 3 intentos para adivinar un numero entre 0 y 99')
intento = 1
while intento < 4 and not gane:
    numeroIngresado = int(input('Ingresa tu numero: '))
    if numeroIngresado == numero_aleatorio:
        print('Ganaste! y necesitaste {} intentos!!!'.format(intento))
        gane = True
    else:
        print('Mmm... No.. ese numero no es... Segui intentando.')
        intento += 1
if not gane:
    print('\n Perdiste :(\n El numero era: {}'.format(numero_aleatorio))
