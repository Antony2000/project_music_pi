import pygame
import time
from pynput import keyboard
import os
import argparse

pygame.init()
os.system("cls")
parser = argparse.ArgumentParser(description='Manual del script')
parser.add_argument('-s','--song', type=str, default = None, required=True)
parser.add_argument('-t','--text', type=str, default = None, required=True)
parser.add_argument('-n','--nomvariable', type=str, default = None, required=True)
args = parser.parse_args()

pygame.mixer.music.load(args.song)
file = open(args.text, "w")

print("Reproduciendo y grabando en 3...")
time.sleep(1)
print("Reproduciendo y grabando en 2...")
time.sleep(1)
print("Reproduciendo y grabando en 1...")
time.sleep(1)
os.system("cls")
pygame.mixer.music.play()


start = time.time()
cont=0
time2=0

def on_press(key):
    if key == keyboard.Key.f12:#SI SE PULSA F12 FINALIZA EL PROGRAMA
        file.close()
        return False
    try:
        global cont
        global time2
        if cont == 0:
            print("time.sleep("+"{:.2f}".format(time.time()-start)+")")
            file.write("time.sleep(" + "{:.2f}".format(time.time() - start) + ")\n")
            cont+=1
        else:
            # AL TIEMPO TOTAL LE RESTAMOS EL TIEMPO QUE ESTA ACTIVO EL GPIO PARA QUE NO HAIGA RETARDOS EN LA MUSICA
            print("time.sleep(" + "{:.2f}".format((time.time()-time2)-float(args.tiempoactivo)) + ")")
            file.write("time.sleep(" + "{:.2f}".format((time.time()-time2)-float(args.tiempoactivo)) + ")\n")

        time2=time.time()
        print("GPIO.output("+args.nomvariable+", True)")
        file.write("GPIO.output(" + args.nomvariable + ", True)\n")
        print("time.sleep("+args.tiempoactivo+")")#CAMBIAR AQUI EL TIEMPO ACTIVO EL GPIO
        file.write("time.sleep(" + args.tiempoactivo + ")\n")  # CAMBIAR AQUI EL TIEMPO ACTIVO EL GPIO
        print("GPIO.output("+args.nomvariable+", False)")
        file.write("GPIO.output(" + args.nomvariable + ", False)\n")

    except AttributeError:
        print('special key pressed: {0}'.format(
            key))

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

# def on_press(key):
#     if key == keyboard.Key.f12:#SI SE PULSA F12 FINALIZA EL PROGRAMA
#         file.close()
#         return False
#     try:
#         global cont
#         global time2
#         if cont == 0:
#             print("time.sleep("+"{:.2f}".format(time.time()-start)+")")
#             file.write("time.sleep(" + "{:.2f}".format(time.time() - start) + ")\n")
#             cont+=1
#         else:
#             # AL TIEMPO TOTAL LE RESTAMOS EL TIEMPO QUE ESTA ACTIVO EL GPIO PARA QUE NO HAIGA RETARDOS EN LA MUSICA
#             print("time.sleep(" + "{:.2f}".format((time.time()-time2)) + ")")
#             file.write("time.sleep(" + "{:.2f}".format((time.time()-time2)) + ")\n")
#
#         time2=time.time()
#         print("GPIO.output("+args.nomvariable+", True)")
#         file.write("GPIO.output(" + args.nomvariable + ", True)\n")
#
#
#     except AttributeError:
#         print('special key pressed: {0}'.format(
#             key))
#
# def on_release(key):
#     global time2
#     print("time.sleep(" + "{:.2f}".format((time.time()-time2)) + ")")  # CAMBIAR AQUI EL TIEMPO ACTIVO EL GPIO
#     file.write("time.sleep(" + "{:.2f}".format((time.time()-time2)) + ")\n")  # CAMBIAR AQUI EL TIEMPO ACTIVO EL GPIO
#     print("GPIO.output(" + args.nomvariable + ", False)")
#     file.write("GPIO.output(" + args.nomvariable + ", False)\n")
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False
#
#
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release
#         ) as listener:
#     listener.join()

