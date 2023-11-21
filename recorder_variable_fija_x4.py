from pygame import mixer
import time
from pynput import keyboard
import os
import argparse

mixer.init()
os.system("cls")

parser = argparse.ArgumentParser(description='Manual del script')
parser.add_argument('-s','--song', type=str, default = None, required=True)
parser.add_argument('-t','--text', type=str, default = None, required=True)
parser.add_argument('-n1','--nomvariable1', type=str, default = None, required=True)
parser.add_argument('-n2','--nomvariable2', type=str, default = None, required=True)
parser.add_argument('-n3','--nomvariable3', type=str, default = None, required=True)
parser.add_argument('-n4','--nomvariable4', type=str, default = None, required=True)
parser.add_argument('-ta','--tiempoactivo', type=str, default = None, required=True)
args = parser.parse_args()

mixer.music.load(args.song)
file = open(args.text, "w")
file.write("import RPi.GPIO as GPIO\n")
file.write("import time\n")
file.write("GPIO.setmode(GPIO.BOARD)\n")
file.write("GPIO.setup("+args.nomvariable1+", GPIO.OUT)\n")
file.write("GPIO.setup("+args.nomvariable2+", GPIO.OUT)\n")
file.write("GPIO.setup("+args.nomvariable3+", GPIO.OUT)\n")
file.write("GPIO.setup("+args.nomvariable4+", GPIO.OUT)\n")

print("Controles:")
print("↑: n1")
print("↓: n2")
print("→: n3")
print("←: n4")
print("F12: Terminar programa")
input("Presione cualquier tecla para continuar...")


print("Reproduciendo y grabando en 3...")
time.sleep(1)
print("Reproduciendo y grabando en 2...")
time.sleep(1)
print("Reproduciendo y grabando en 1...")
time.sleep(1)
os.system("cls")
mixer.music.play()


start = time.time()
cont=0
time2=0

def on_press(key):
    global start
    global cont
    global time2
    if key == keyboard.Key.f12:#SI SE PULSA F12 FINALIZA EL PROGRAMA
        file.close()
        return False
    if key == keyboard.Key.up:
        if cont == 0:
            print("time.sleep("+"{:.2f}".format(time.time()-start)+")")
            file.write("time.sleep(" + "{:.2f}".format(time.time() - start) + ")\n")
            cont+=1
        else:
            # AL TIEMPO TOTAL LE RESTAMOS EL TIEMPO QUE ESTA ACTIVO EL GPIO PARA QUE NO HAIGA RETARDOS EN LA MUSICA
            print("time.sleep(" + "{:.2f}".format((time.time()-time2)-float(args.tiempoactivo)) + ")")
            file.write("time.sleep(" + "{:.2f}".format((time.time()-time2)-float(args.tiempoactivo)) + ")\n")

        time2=time.time()
        print("GPIO.output("+args.nomvariable1+", False)")
        file.write("GPIO.output(" + args.nomvariable1 + ", False)\n")
        print("time.sleep("+args.tiempoactivo+")")#CAMBIAR AQUI EL TIEMPO ACTIVO EL GPIO
        file.write("time.sleep(" + args.tiempoactivo + ")\n")  # CAMBIAR AQUI EL TIEMPO ACTIVO EL GPIO
        print("GPIO.output("+args.nomvariable1+", True)")
        file.write("GPIO.output(" + args.nomvariable1 + ", True)\n")

    if key == keyboard.Key.down:

        if cont == 0:
            print("time.sleep(" + "{:.2f}".format(time.time() - start) + ")")
            file.write("time.sleep(" + "{:.2f}".format(time.time() - start) + ")\n")
            cont += 1
        else:
            # AL TIEMPO TOTAL LE RESTAMOS EL TIEMPO QUE ESTA ACTIVO EL GPIO PARA QUE NO HAIGA RETARDOS EN LA MUSICA
            print("time.sleep(" + "{:.2f}".format((time.time() - time2) - float(args.tiempoactivo)) + ")")
            file.write("time.sleep(" + "{:.2f}".format((time.time() - time2) - float(args.tiempoactivo)) + ")\n")

        time2 = time.time()
        print("GPIO.output(" + args.nomvariable2 + ", False)")
        file.write("GPIO.output(" + args.nomvariable2 + ", False)\n")
        print("time.sleep(" + args.tiempoactivo + ")")  # CAMBIAR AQUI EL TIEMPO ACTIVO EL GPIO
        file.write("time.sleep(" + args.tiempoactivo + ")\n")  # CAMBIAR AQUI EL TIEMPO ACTIVO EL GPIO
        print("GPIO.output(" + args.nomvariable2 + ", True)")
        file.write("GPIO.output(" + args.nomvariable2 + ", True)\n")

    if key == keyboard.Key.right:
        # global cont
        # global time2
        if cont == 0:
            print("time.sleep(" + "{:.2f}".format(time.time() - start) + ")")
            file.write("time.sleep(" + "{:.2f}".format(time.time() - start) + ")\n")
            cont += 1
        else:
            # AL TIEMPO TOTAL LE RESTAMOS EL TIEMPO QUE ESTA ACTIVO EL GPIO PARA QUE NO HAIGA RETARDOS EN LA MUSICA
            print("time.sleep(" + "{:.2f}".format((time.time() - time2) - float(args.tiempoactivo)) + ")")
            file.write("time.sleep(" + "{:.2f}".format((time.time() - time2) - float(args.tiempoactivo)) + ")\n")

        time2 = time.time()
        print("GPIO.output(" + args.nomvariable3 + ", False)")
        file.write("GPIO.output(" + args.nomvariable3 + ", False)\n")
        print("time.sleep(" + args.tiempoactivo + ")")  # CAMBIAR AQUI EL TIEMPO ACTIVO EL GPIO
        file.write("time.sleep(" + args.tiempoactivo + ")\n")  # CAMBIAR AQUI EL TIEMPO ACTIVO EL GPIO
        print("GPIO.output(" + args.nomvariable3 + ", True)")
        file.write("GPIO.output(" + args.nomvariable3 + ", True)\n")

    if key == keyboard.Key.left:
        # global cont
        # global time2
        if cont == 0:
            print("time.sleep(" + "{:.2f}".format(time.time() - start) + ")")
            file.write("time.sleep(" + "{:.2f}".format(time.time() - start) + ")\n")
            cont += 1
        else:
            # AL TIEMPO TOTAL LE RESTAMOS EL TIEMPO QUE ESTA ACTIVO EL GPIO PARA QUE NO HAIGA RETARDOS EN LA MUSICA
            print("time.sleep(" + "{:.2f}".format((time.time() - time2) - float(args.tiempoactivo)) + ")")
            file.write("time.sleep(" + "{:.2f}".format((time.time() - time2) - float(args.tiempoactivo)) + ")\n")

        time2 = time.time()
        print("GPIO.output(" + args.nomvariable4 + ", False)")
        file.write("GPIO.output(" + args.nomvariable4 + ", False)\n")
        print("time.sleep(" + args.tiempoactivo + ")")  # CAMBIAR AQUI EL TIEMPO ACTIVO EL GPIO
        file.write("time.sleep(" + args.tiempoactivo + ")\n")  # CAMBIAR AQUI EL TIEMPO ACTIVO EL GPIO
        print("GPIO.output(" + args.nomvariable4 + ", True)")
        file.write("GPIO.output(" + args.nomvariable4 + ", True)\n")

    # try:
    #
    # except AttributeError:
    #     print('special key pressed: {0}'.format(
    #         key))

# def on_release(key):
#     print('Key released: {0}'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False


with keyboard.Listener(
        on_press=on_press,
        #on_release=on_release
        ) as listener:
    listener.join()



