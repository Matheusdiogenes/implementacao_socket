#!/usr/bin/env python3

import socket
import threading
import uuid

def main():
  HOST = 'localhost'
  PORT = 8081
  orig = (HOST, PORT)

  tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  tcp.bind(orig)
  tcp.listen()  
  qtde_token = int(input("Quantidade de token: "))
  while True:
    print('Aguardando conexão...')
    conn, cliente = tcp.accept()
    print(f'Conectado com o cliente: {cliente}')
    data = conn.recv(1024)    
    print(f'Cliente: {cliente}\n')    
    if '2' == data.decode('utf-8'):      
      info = (str(qtde_token) + ' tokens disponiveis')
      conn.send(info.encode('utf-8')) # Envia mensagem
    
    qtde_token -= 1    
    conn.sendall(data)  
    

if __name__ == "__main__":
  main()