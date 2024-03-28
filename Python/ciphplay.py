import sys
import os


clear = lambda: os.system('clear')
text = input()
if text == "cake":
    clear ()
    print("The cake is a lie")
elif text == "Wash":
    clear ()
    print("Im a leaf on the wind, watch how I soar.")
else:
    clear ()
    print ("Entered Text (no reaction)")
    print (text)