from pygame import mixer
import os
import time
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
args = parser.parse_args()

GPIO_on_1= 'GPIO.output(' + args.nomvariable1 + ', True)'
GPIO_off_1= 'GPIO.output(' + args.nomvariable1 + ', False)'
GPIO_on_2= 'GPIO.output(' + args.nomvariable2 + ', True)'
GPIO_off_2= 'GPIO.output(' + args.nomvariable2 + ', False)'
GPIO_on_3= 'GPIO.output(' + args.nomvariable3 + ', True)'
GPIO_off_3= 'GPIO.output(' + args.nomvariable3 + ', False)'
GPIO_on_4= 'GPIO.output(' + args.nomvariable4 + ', True)'
GPIO_off_4= 'GPIO.output(' + args.nomvariable4 + ', False)'

mixer.music.load(args.song)
file = open(args.text, "r")
Lines=file.readlines()

print("Reproduciendo en 3...")
time.sleep(1)
print("Reproduciendo en 2...")
time.sleep(1)
print("Reproduciendo en 1...")
time.sleep(1)
os.system("cls")

mixer.music.play()
for line in Lines:
    if line.strip() == GPIO_on_1.strip():
        print("ON         ", end="\r")
    if line.strip() == GPIO_off_1.strip():
        print("           ", end="\r")
    if line.strip() == GPIO_on_2.strip():
        print("   ON      ", end="\r")
    if line.strip() == GPIO_off_2.strip():
        print("           ", end="\r")
    if line.strip() == GPIO_on_3.strip():
        print("      ON   ", end="\r")
    if line.strip() == GPIO_off_3.strip():
        print("           ", end="\r")
    if line.strip() == GPIO_on_4.strip():
        print("         ON", end="\r")
    if line.strip() == GPIO_off_4.strip():
        print("           ", end="\r")
    if line.strip().startswith("time.sleep("):
        exec(line)

