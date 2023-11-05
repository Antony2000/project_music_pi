import RPi.GPIO as GPIO
import os
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

bucle=True
while bucle:
    os.system("clear")
    gpio=int(input("Introduzca el relé que desea encender (Introduzca 0 para salir del programa): "))

    if gpio == 0:
        bucle=False
    elif gpio == 1:
        GPIO.output(3, False)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(3, True)
    elif gpio == 2:
        GPIO.output(5, False)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(5, True)
    elif gpio == 3:
        GPIO.output(7, False)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(7, True)
    elif gpio == 4:
        GPIO.output(8, False)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(8, True)
    elif gpio == 5:
        GPIO.output(10, False)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(10, True)
    elif gpio == 6:
        GPIO.output(11, False)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(11, True)
    elif gpio == 7:
        GPIO.output(12, False)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(12, True)
    elif gpio == 8:
        GPIO.output(13, False)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(13, True)
    elif gpio == 9:
        GPIO.output(15, False)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(15, True)
    elif gpio == 10:
        GPIO.output(16, False)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(16, True)
    elif gpio == 11:
        GPIO.output(18, False)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(18, True)
    elif gpio == 12:
        GPIO.output(19, False)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(19, True)
    elif gpio == 13:
        GPIO.output(21, False)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(21, True)
    elif gpio == 14:
        GPIO.output(22, False)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(22, True)
    elif gpio == 15:
        GPIO.output(23, False)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(23, True)
    elif gpio == 16:
        GPIO.output(24, False)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(24, True)
    elif gpio < 0 or gpio > 16:
        print("Error: no es un numero valido (Rele entre 1 y 16)")
        input("Presione cualquier tecla para continuar...")
