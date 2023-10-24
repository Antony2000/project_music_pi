from pygame import mixer
import os
import argparse
from pynput import keyboard
mixer.init()
os.system("cls")

parser = argparse.ArgumentParser(description='Manual del script')
parser.add_argument('-s','--song', type=str, default = None, required=True)
args = parser.parse_args()
mixer.music.load(args.song)

def on_press(key):
    if key == keyboard.Key.f10:
        return False
    if key == keyboard.Key.f12:
        mixer.music.play()

with keyboard.Listener(
        on_press=on_press,
        #on_release=on_release
        ) as listener:
    listener.join()


