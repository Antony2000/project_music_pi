import RPi.GPIO as GPIO
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
    gpio=int(input("Introduzca el relé que desea encender (Introduzca 0 para salir del programa): "))

    if gpio == 0:
        bucle==False
    elif gpio == 1:
        GPIO.output(3, True)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(3, False)
    elif gpio == 2:
        GPIO.output(5, True)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(5, False)
    elif gpio == 3:
        GPIO.output(7, True)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(7, False)
    elif gpio == 4:
        GPIO.output(8, True)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(8, False)
    elif gpio == 5:
        GPIO.output(10, True)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(10, False)
    elif gpio == 6:
        GPIO.output(11, True)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(11, False)
    elif gpio == 7:
        GPIO.output(12, True)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(12, False)
    elif gpio == 8:
        GPIO.output(13, True)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(13, False)
    elif gpio == 9:
        GPIO.output(15, True)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(15, False)
    elif gpio == 10:
        GPIO.output(16, True)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(16, False)
    elif gpio == 11:
        GPIO.output(18, True)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(18, False)
    elif gpio == 12:
        GPIO.output(19, True)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(19, False)
    elif gpio == 13:
        GPIO.output(21, True)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(21, False)
    elif gpio == 14:
        GPIO.output(22, True)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(22, False)
    elif gpio == 15:
        GPIO.output(23, True)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(23, False)
    elif gpio == 16:
        GPIO.output(24, True)
        input("Presione cualquier tecla para continuar...")
        GPIO.output(24, False)
    elif gpio < 0 or gpio > 16:
        print("Error: no es un numero valido (Rele entre 1 y 16)")
