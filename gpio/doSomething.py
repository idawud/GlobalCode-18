from subprocess import call
from gpiozero import Button
from signal import pause

def doSomething():
    print("Hello, ")

button = Button(2)

button.when_pressed = doSomething
pause()