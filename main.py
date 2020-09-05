import pynput

from pynput.keyboard import Key, Listener


def on_press(key):
    print("{0} pressed".format(key))


with Listener(on_press =on_press, on_release=on_release) as listener:
    listener.join()