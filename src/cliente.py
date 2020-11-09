#!/usr/bin/env python3

import socket

HOST = 'localhost'
PORT = 8081

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.connect(orig)
tcp.send(str.encode('Sou cliente'))
data = tcp.recv(1024)

print(f'Dados: {data.decode()}')