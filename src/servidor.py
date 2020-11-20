#!/usr/bin/env python3

import socket
def main():
  HOST = 'localhost'
  PORT = 8081

  tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  orig = (HOST, PORT)
  tcp.bind(orig)
  tcp.listen()

  while True:
    print('Aguardando conexão...')
    conn, cliente = tcp.accept()
    print(f'Conectado com o cliente: {cliente}')
    while True:
      data = conn.recv(1024)
      if not data:
        print('Fechando conexão')
        conn.close()
        break
      print(f'Cliente: {cliente}\nDados:{data}')
      conn.sendall(data)  

if __name__ == "__main__":
  main()