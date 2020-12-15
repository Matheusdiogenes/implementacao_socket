#!/usr/bin/env python3

import socket


def main():
  HOST = 'localhost'
  PORT = 8081
  # Invocando o socket(familia ipv4, tcp)
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # Conectando ao socket do servidor
  sock.connect((HOST, PORT))
  while True:  
    print(f'1) Solicitar Token (3 -1)\n2) Devolver token (5 X) \n3) Quantidade de recursos disponíveis (1 -1) \n')
    msg = input('Insira a opção escolhida:  ')
    # Envia solicitação
    if not msg:
      break
    sock.send(str.encode(msg))    
    # Resposta do servidor
    info = sock.recv(1024)
    print(info.decode('utf-8'))  


if __name__ == "__main__":
  main()