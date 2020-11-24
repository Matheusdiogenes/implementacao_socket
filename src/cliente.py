#!/usr/bin/env python3

import socket
import uuid

def main():
  HOST = 'localhost'
  PORT = 8081
  tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  orig = (HOST, PORT)
  tcp.connect(orig)
  
  print(f'1) Solicitar Token (3 -1)\n2) Devolver token \n3) Quantidade de recursos disponíveis (1 -1)   \n')
  msg = input('Insira a opção escolhida:  ')
  tcp.send(str.encode(msg))    
  info = tcp.recv(1024)
  print(info.decode('utf-8'))  


if __name__ == "__main__":
  main()