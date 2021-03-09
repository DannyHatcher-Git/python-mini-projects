import pynput

print(dir(pynput.keyboard)) # List the keyboard inputs
print(dir(pynput)) # List the pynput options
print(dir(pynput.mouse)) # List the moust inputs
print(type(pynput)) # Printing the type of the thing (thing in here)
print(type(pynput.mouse)) # Printing module inside a module
print(type(pynput.mouse.Controller)) # Printing all

from pynput.keyboard import Key, Controller

keyboard = Controller()

keyboard.press(Key.space)
keyboard.release(Key.sapce)
