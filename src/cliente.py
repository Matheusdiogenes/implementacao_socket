#!/usr/bin/env python3

import socket
import uuid

def main():
  HOST = 'localhost'
  PORT = 8081
  tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  orig = (HOST, PORT)
  tcp.connect(orig)
  tcp.send(str.encode(uuid.uuid4().hex))
  data = tcp.recv(1024)
  print(f'Dados: {data.decode()}')


if __name__ == "__main__":
  main()