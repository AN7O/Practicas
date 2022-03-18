# Adivina adivinador....
import random
numero_aleatorio = random.randrange(100)
gane = False
print('Tenes 3 intentos para adivinar un numero entre 0 y 99')
intento = 0
while intento < 5 and not gane:
    numero_ingresado = int(input('Ingresa tu numero: '))
    if numero_ingresado == numero_aleatorio:
        print('Ganaste! y necesitaste {} intentos!!!'.format(intento))
        gane = True
    else:
        print('Mmm... No.. ese numero no es... Segui intentando.')
        intento += 1
if not gane:
    print('\n Perdiste :(\n El numero era: {}'.format(numero_aleatorio))
