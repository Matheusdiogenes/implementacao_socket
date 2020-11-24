#!/usr/bin/env python3

import socket
from _thread import *
import uuid
import socket


def conecta(conn, qtde_token):
  control = qtde_token
  while True:
    data = conn.recv(1024)        
    if '1' == data.decode('utf-8'):      
      if qtde_token > 0:
        token = uuid.uuid4().hex
        conn.send(token.encode())
        qtde_token -= 1
      else:
        info = 'Rucurso não disponivel'
        conn.send(info.encode())        
    elif '2' == data.decode('utf-8'):
      if qtde_token < control:
        qtde_token += 1
        info = 'Token devolvido'
        conn.send(info.encode())        
      else:
        info = 'Rucurso não disponivel'
        conn.send(info.encode())        
    elif '3' == data.decode('utf-8'):
        info = (str(qtde_token) + ' tokens disponiveis')
        conn.send(info.encode('utf-8'))     
    


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
    start_new_thread(conecta, (conn,qtde_token,)) 
      

if __name__ == "__main__":
  main()