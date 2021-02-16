#!/usr/bin/env python3

from queue import Queue
import socket
import threading

target = "127.0.0.1"
queue = Queue()
open_ports = []

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        return True
    except:
        return False
def get_ports(mode):
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)
    elif mode == 2:
        for port in range(1, 49152):
            queue.put(port)

    elif mode == 3:
        ports = [##portsyou want to scan]
        for port in ports:
            queue.put(port)
    elif == mode 4:
        ports = ("Enter your ports(separate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("port {} is open".format(port))
            open_ports.append(port)
        else:
            print("port {} is closed".format(port))
def run_scanner(threads, mode):
    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    print("Open ports are: ", open_ports)

#######run_scanner(100, 1)
