from pygame import mixer
import os
import time
import argparse


mixer.init()
os.system("cls")

parser = argparse.ArgumentParser(description='Manual del script')
parser.add_argument('-s','--song', type=str, default = None, required=True)
parser.add_argument('-t','--text', type=str, default = None, required=True)
parser.add_argument('-n','--nomvariable', type=str, default = None, required=True)
args = parser.parse_args()

GPIO_on= 'GPIO.output(' + args.nomvariable + ', True)'
GPIO_off= 'GPIO.output(' + args.nomvariable + ', False)'

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
    if line.strip() == GPIO_on.strip():
        print("ON", end="\r")
    elif line.strip() == GPIO_off.strip():
        print("  ", end="\r")
    else:
        exec(line)

