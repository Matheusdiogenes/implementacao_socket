#!/usr/bin/env python3

import socket

import threading
import uuid
import socket


def conecta(conn, qtde_token):
  aux = qtde_token
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
      if qtde_token < aux:
        qtde_token += 1
        info = 'Token devolvido'
        conn.send(info.encode())
      else:
        info = 'Rucurso não disponivel'
        conn.send(info.encode())        
    elif '3' == data.decode('utf-8'):
        info = (str(qtde_token) + ' tokens disponiveis')
        conn.send(info.encode('utf-8'))
    else:
        info = 'Comando não encontrado'
        conn.send(info.encode())            



def main():
  HOST = 'localhost'
  PORT = 8081  
  # Invocando o socket(ipv4, tcp)
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # Porta a escutar
  sock.bind((HOST, PORT))
  sock.listen()  
   
  global qtde_token = int(input("Quantidade de token: "))      
  while True:
    print('Aguardando conexão...')
    # aceitando a conexão
    conn, endereco = sock.accept()    
    print(f'Conectado com o cliente no endereço: {endereco}')    
    # abrindo threads 
    threading.Thread(target=conecta, args=(conn, qtde_token)).start()
    

    
      

if __name__ == "__main__":  
  main()