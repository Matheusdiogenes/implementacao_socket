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
    print(f'1) Solicitar Token (3 -1) \n2) Devolver token (5 X) \n3) Solicita quantidade de recursos disponíveis (1 -1)   \n')
    msg = input('Insira a opção escolhida:  ')
    tcp.send(str.encode(msg))
    # data = tcp.recv(1024)    
    info = tcp.recv(1024)
    print(info.decode('utf-8'))



if __name__ == "__main__":
  main()