from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener

mouse = Controller()


def on_press(key):
    if key == Key.shift:
        mouse.click(Button.left)


def on_release(key):
    pass


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
