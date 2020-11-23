#!/usr/bin/env python3

import socket
import uuid

def main():
  HOST = 'localhost'
  PORT = 8081
  tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  orig = (HOST, PORT)
  tcp.connect(orig)
  # tcp.send(str.encode(uuid.uuid4().hex))
  while True:
    print(f'1) Solicitar Token (3 -1) \n2) Solicita quantidade de recursos disponíveis (1 -1)   \n')
    msg = input('Insira a opção escolhida:  ')
    tcp.send(str.encode(msg))    
    info = tcp.recv(1024)
    if msg == '2':
      print(info.decode('utf-8'))
      break
      


if __name__ == "__main__":
  main()