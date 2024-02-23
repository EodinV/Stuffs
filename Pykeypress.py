from pynput import keyboard
from pynput.keyboard import Key
import os
import sys

clear = lambda: os.system('clear')
def on_key_release(key):
    if key == Key.right:
        clear ()
        print("Right key clicked")
    elif key == Key.left:
        clear ()
        print("Left key clicked")
    elif key == Key.up:
        clear ()
        print("Up key clicked")
    elif key == Key.down:
        clear ()
        print("Down key clicked")
    elif key == Key.esc:
        clear ()
        exit()


with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()